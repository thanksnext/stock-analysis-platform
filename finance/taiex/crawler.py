import datetime
import logging
import random
import time

import requests
from constance import config
from holiday.models import Holiday

from .models import Taiex

logger = logging.getLogger(__name__)


class TaiexCrawler:
    taiex_url = (
        "http://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date={}"
    )

    volume_url = "https://www.twse.com.tw/exchangeReport/FMTQIK?response=json&date={}"

    def __init__(self):
        self.start_date = getattr(config, "CRAWLER_TAIEX_START_DATE")
        self.crawler_min_interval = getattr(config, "CRAWLER_MIN_INTERVAL")
        self.crawler_max_interval = getattr(config, "CRAWLER_MAX_INTERVAL")

    def crawl(self):  # pragma: no cover
        holiday_list = self.get_holiday_list()

        while self.start_date <= datetime.date.today():
            if self.start_date in holiday_list or self.start_date.isoweekday() in [
                6,
                7,
            ]:
                logger.info(
                    f"Crawling date ({self.start_date}) of taiex is holiday, skip it."
                )
                self.start_date += datetime.timedelta(1)
                setattr(config, "CRAWLER_TAIEX_START_DATE", self.start_date)
                continue

            try:
                date = datetime.datetime.strftime(self.start_date, "%Y%m%d")
                taiex_responses = self.start_requests(date, self.taiex_url)
                time.sleep(
                    random.uniform(self.crawler_min_interval, self.crawler_max_interval)
                )
                volume_response = self.start_requests(date, self.volume_url)
                combine_data = self.combine(
                    taiex=taiex_responses, volume=volume_response
                )
                combine_data = self.parse(combine_data)
                self.save_data(combine_data)

                self.start_date += datetime.timedelta(1)
                setattr(config, "CRAWLER_TAIEX_START_DATE", self.start_date)
                time.sleep(
                    random.uniform(self.crawler_min_interval, self.crawler_max_interval)
                )
            except requests.exceptions.RequestException as e:
                logger.error(e)
                break

    def start_requests(self, date, url):
        try:
            r = requests.get(url.format(date))
            res = r.json()

            if r.status_code == requests.codes.ok and res["stat"] == "OK":
                return res["data"]
            else:
                return []
        except requests.exceptions.RequestException as e:
            raise e

    def parse(self, data):
        taiex = []

        for _taiex in data:
            year, month, day = map(int, _taiex[0].strip().split("/"))
            year += 1911
            _taiex[0] = "-".join(map(str, [year, month, day]))
            if datetime.date(year, month, day) >= self.start_date:
                _taiex[1:] = [price.replace(",", "") for price in _taiex[1:]]
                taiex.append(_taiex)

        return taiex

    def combine(self, **kargs):
        combine_data = []
        for _taiex, _volume in zip(kargs["taiex"], kargs["volume"]):
            if _taiex[0] == _volume[0]:
                combine_per_date = _taiex + _volume[1:4]
                combine_data.append(combine_per_date)
            else:
                break

        return combine_data

    def save_data(self, taiex):
        for _taiex in taiex:
            row = Taiex.objects.create_taiex(*_taiex)
            row.save()
            logger.info(f"{row.trade_date} taiex saved")
            self.start_date = datetime.datetime.strptime(
                row.trade_date, "%Y-%m-%d"
            ).date()
            setattr(config, "CRAWLER_TAIEX_START_DATE", self.start_date)

    def get_holiday_list(self):
        holiday_list = Holiday.objects.values_list("date", flat=True)
        return holiday_list
