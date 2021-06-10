import datetime
import logging
import time

import fundamentals.config as cf
import pandas as pd
import requests
from company.models import Company
from constance import config
from holiday.models import Holiday

from .models import BalanceSheet, ComprehensiveIncome, YearSeasonTableInfo

logger = logging.getLogger("finance")


def get_season(date):
    stockDate = [
        ["4-30", "5-15", "5-30"],
        ["8-14", "8-31"],
        ["10-31", "11-14", "11-29"],
        ["3-31"],
    ]

    for seasonIdx in range(len(stockDate)):
        if date in stockDate[seasonIdx]:
            return seasonIdx + 1

    return -1


def get_holiday_list():
    holiday_list = Holiday.objects.values_list("date", flat=True)
    return holiday_list


# 綜合損益彙總表 資產負債表
class BalanceSheetAndIncomeStatementCrawler:
    def __init__(self, paramObj):

        self.targetDate = None
        self.targetDateStr = ""
        if paramObj == "Income":
            self.targetDateStr = "CRAWLER_STOCK_START_DATE_COMPREHENSIVE"
            self.urlBase = "https://mops.twse.com.tw/mops/web/ajax_t163sb04"
            self.targetDuplicate = cf.incomeInstatementDuplicate
            self.AttrC2E = cf.statementIncomeC2E
            self.targetDatabase = ComprehensiveIncome
        else:
            self.targetDateStr = "CRAWLER_STOCK_START_DATE_BALANCE"
            self.urlBase = "https://mops.twse.com.tw/mops/web/ajax_t163sb05"
            self.targetDuplicate = cf.balanceSheetDuplicate
            self.AttrC2E = cf.balanceSheetC2E
            self.targetDatabase = BalanceSheet

        # get date for next crawler
        self.format_pattern = "%Y-%m-%d"
        self.checkCrawler = False

        self.today_str = datetime.datetime.now().strftime(self.format_pattern)
        self.endLoop = False

        # crawler_min_interval = getattr(config, "CRAWLER_MIN_INTERVAL")
        # crawler_max_interval = getattr(config, "CRAWLER_MAX_INTERVAL")

        self.headers = {
            "Connection": "close",
        }
        self.maxEntry = 0

    def start_requests(self):
        while self.maxEntry <= 5:
            try:
                r = requests.post(self.urlBase, data=self.payload, headers=self.headers)
                r.encoding = "utf8"
                return r
            except requests.exceptions.RequestException as e:
                logger.error(self.urlBase + " connection error")
                logger.error(e)
                logger.error("sleep 10 s")
                time.sleep(10)
                logger.error("try again")
                self.maxEntry += 1
                continue

    def parse(self, data, year, season, rowNum):

        read_data = data
        read_data_df = pd.concat(read_data[rowNum : rowNum + 1], axis=0, sort=False)
        # 把重複的欄位換名字
        read_data_df = read_data_df.rename(columns=self.targetDuplicate)
        # 補齊欄位及固定欄位
        dtypes = ["object", "object"]
        fixAttr = ["公司代號", "公司名稱"]
        for idx in self.AttrC2E:
            fixAttr.append(self.AttrC2E[idx])
            if idx not in read_data_df.columns:
                read_data_df[idx] = None
                dtypes.append("object")
            else:
                read_data_df[idx] = read_data_df[idx].replace("--", -1)
                dtypes.append("float")

        fixAttr.append("company_id")
        fixAttr.append("year_season_id")

        read_data_df["company_id"] = 0
        dtypes.append("object")
        read_data_df["year_season_id"] = 0
        dtypes.append("object")

        # 欄位中翻英
        read_data_df = read_data_df.rename(columns=self.AttrC2E)

        read_data_df = read_data_df[fixAttr]
        columns = list(read_data_df)
        columns_dtype = dict(zip(columns, dtypes))
        read_data_df = read_data_df.astype(columns_dtype)

        return read_data_df

    def crawler_detail(self):
        if self.payload["year"] < 2013:
            return

        if self.payload["year"] >= 1000:
            self.payload["year"] -= 1911

        response = self.start_requests()

        response_data = pd.read_html(response.text, header=None)

        for idx in range(1, len(response_data), 1):
            data_parse = self.parse(
                response_data, self.payload["year"], self.payload["season"], idx
            )
            self.save_data(data_parse, idx)

        return data_parse

    def crawl(self):
        holiday_list = get_holiday_list()

        while not self.endLoop:
            self.targetDate = getattr(config, self.targetDateStr)
            start_date = str(self.targetDate)
            logger.debug("start: " + start_date)
            logger.debug(
                "crawler day: "
                + str(self.targetDate.year)
                + "-"
                + str(self.targetDate.month)
                + "-"
                + str(self.targetDate.day)
            )
            self.endLoop = False

            # If crawling date is holiday
            if self.targetDate in holiday_list or self.targetDate.isoweekday() in [
                6,
                7,
            ]:
                logger.info(f"Crawling date ({self.targetDate}) is holiday, skip it.")
                self.targetDate += datetime.timedelta(1)
                setattr(config, self.targetDateStr, self.targetDate)
                continue

            if datetime.datetime.strptime(
                self.today_str, self.format_pattern
            ) > datetime.datetime.strptime(start_date, self.format_pattern):
                getSeason = get_season(
                    str(self.targetDate.month) + "-" + str(self.targetDate.day)
                )
                if getSeason != -1:
                    self.checkCrawler = True
                    logger.debug("ready for crawler")
                else:
                    self.checkCrawler = False
                    logger.debug("not in season list and add 1")
                    self.targetDate += datetime.timedelta(1)
                    setattr(config, self.targetDateStr, self.targetDate)
                    logger.debug("-" * 20)
            else:
                self.checkCrawler = False
                self.endLoop = True
                logger.debug("don't crawler")
                logger.debug("-" * 20)

            if self.checkCrawler:
                getYear = self.targetDate.year

                if getSeason == 4:
                    getYear = getYear - 1

                # crawl stock
                self.crawler_year, self.crawler_season = str(getYear), str(getSeason)

                self.payload = {
                    "encodeURIComponent": 1,
                    "step": 1,
                    "firstin": 1,
                    "off": 1,
                    "TYPEK": "sii",
                    "year": int(self.crawler_year),
                    "season": int(self.crawler_season),
                }
                self.crawler_detail()

                self.targetDate += datetime.timedelta(1)
                setattr(config, self.targetDateStr, self.targetDate)
                logger.debug("Crawler end")
                logger.debug("-" * 20)
                time.sleep(10)

    def save_data(self, data, companyType):

        # 處理年份及季節的部份，若沒有就插入
        yearDetail = list(
            YearSeasonTableInfo.objects.filter(year=self.payload["year"]).filter(
                season=self.payload["season"]
            )
        )
        if len(yearDetail) == 0:
            yearData = [self.payload["year"], self.payload["season"]]
            saveyearData = YearSeasonTableInfo.objects.create_ci(*yearData)
            saveyearData.save()
            getYearId = list(
                YearSeasonTableInfo.objects.filter(year=self.payload["year"]).filter(
                    season=self.payload["season"]
                )
            )[0].id
        else:
            getYearId = yearDetail[0].id

        for index, row in data.iterrows():
            companyDetail = list(Company.objects.filter(company_code=row["公司代號"]))
            getCompanyId = companyDetail[0].id
            row = row.drop(labels=["公司代號", "公司名稱"])

            for idx in range(len(row.index)):
                if row[idx] == -1:
                    row[idx] = None
            row["company_id"] = getCompanyId
            row["year_season_id"] = getYearId
            targetDetail = list(
                self.targetDatabase.objects.filter(company_id=getCompanyId).filter(
                    year_season_id=getYearId
                )
            )

            if targetDetail == []:
                saveStatementIncomeData = self.targetDatabase.objects.create_ci(*row)
                saveStatementIncomeData.save()
