import calendar
import datetime
import logging
import queue
import random
import threading
import time

import requests

# from .models import Stock
from company.models import Company
from constance import config
from holiday.models import Holiday

logger = logging.getLogger(__name__)


class StockCrawler:
    stock_url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?date={}&stockNo={}"

    def __init__(self):
        self.start_date = getattr(config, "CRAWLER_STOCK_START_DATE")
        self.crawler_min_interval = getattr(config, "CRAWLER_MIN_INTERVAL")
        self.crawler_max_interval = getattr(config, "CRAWLER_MAX_INTERVAL")

    def crawl(self, company_code, date):  # pragma: no cover
        try:
            time.sleep(
                random.uniform(self.crawler_min_interval, self.crawler_max_interval)
            )
            company = Company.objects.get(company_code=company_code)
            stock_responses = self.start_requests(date, company_code, self.stock_url)
            data = self.parse(stock_responses, date)
            self.save_data(data, company)

            # self.start_date += datetime.timedelta(1)
            # setattr(config, "CRAWLER_STOCK_START_DATE", self.start_date)

        except requests.exceptions.RequestException as e:
            logger.error(e)

    def start_requests(self, date, code, url):
        flag = True
        while flag:
            try:
                r = requests.get(url.format(date, code))
                res = r.json()
                if r.status_code == requests.codes.ok and res["stat"] == "OK":
                    flag = False
                    return res["data"]
                elif r.status_code == 302:
                    pass
                else:
                    flag = False
                    return []
            except requests.exceptions.RequestException as e:
                raise e

    def parse(self, data, date):
        stock = []

        for _stock in data:
            year, month, day = map(int, _stock[0].strip().split("/"))
            year += 1911
            _stock[0] = "-".join(map(str, [year, month, day]))
            constance_date = datetime.datetime.strptime(date, "%Y%m%d").date()
            constance_year = constance_date.year
            constance_month = constance_date.month
            constance_first_day, constance_last_day = calendar.monthrange(
                constance_year, constance_month
            )
            if (
                datetime.date(constance_year, constance_month, constance_last_day)
                >= datetime.date(year, month, day)
                >= constance_date
            ):
                _stock[1:] = [price.replace(",", "") for price in _stock[1:]]
                _stock[1:] = [None if price == "--" else price for price in _stock[1:]]
                _stock = _stock[0:1] + _stock[3:7] + _stock[1:3] + _stock[8:]
                stock.append(_stock)

        return stock

    def save_data(self, stock, company):
        for _stock in stock:
            row = company.stock.create_stock(*_stock)
            row.save()
            logger.info(f"{row.trade_date} stock({company.company_code}) saved")
            trade_date = datetime.datetime.strptime(row.trade_date, "%Y-%m-%d").date()
            if trade_date > self.start_date:
                self.start_date = trade_date
            # setattr(config, "CRAWLER_STOCK_START_DATE", self.start_date)

    def get_company_code_list(self):
        company_code_list = Company.objects.values_list("company_code", flat=True)
        return company_code_list

    def get_holiday_list(self):
        holiday_list = Holiday.objects.values_list("date", flat=True)
        return holiday_list

    def main(self):
        company_code_list = self.get_company_code_list()
        holiday_list = self.get_holiday_list()

        while self.start_date <= datetime.date.today():
            if self.start_date in holiday_list or self.start_date.isoweekday() in [
                6,
                7,
            ]:
                logger.info(
                    f"Crawling date ({self.start_date}) of stock is holiday, skip it."
                )
                self.start_date += datetime.timedelta(1)
                setattr(config, "CRAWLER_STOCK_START_DATE", self.start_date)
                continue

            try:
                date = datetime.datetime.strftime(self.start_date, "%Y%m%d")
                # 建立佇列
                company_code_queue = queue.Queue()

                # 將資料放入佇列
                for i in company_code_list:
                    company_code_queue.put(i)

                # 建立Worker
                workers = Worker(
                    queue=company_code_queue, func=self.crawl, date=date, num=3
                ).create_worker()

                # 讓 Worker 開始處理資料
                for worker in workers:
                    worker.start()

                # 等待所有 Worker 結束
                for worker in workers:
                    worker.join()

                self.start_date += datetime.timedelta(1)
                setattr(config, "CRAWLER_STOCK_START_DATE", self.start_date)

            except requests.exceptions.RequestException as e:
                logger.error(e)
                break


class Worker(threading.Thread):
    def __init__(self, queue, func, date, num):
        threading.Thread.__init__(self)
        self.queue = queue
        self.func = func
        self.date = date
        self.num = num

    def run(self):
        while self.queue.qsize() > 0:
            # 取得新的資料
            code = self.queue.get()

            # 處理資料
            self.func(code, self.date)

    def create_worker(self):
        workers = []

        for worker in range(0, self.num):
            workers.append(Worker(self.queue, self.func, self.date, self.num))

        return workers
