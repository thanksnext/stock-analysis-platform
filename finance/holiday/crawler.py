import io
import logging
import time
from datetime import date, timedelta

import pandas as pd
import requests
from constance import config

from .models import Holiday

logger = logging.getLogger("finance")


# 公司
class HolidayCrawler:
    def __init__(self):
        self.url = "https://www.twse.com.tw/zh/holidaySchedule/holidaySchedule"
        print(type(getattr(config, "CRAWLER_HOLIDAY_START_DATE")))
        self.start_date = getattr(config, "CRAWLER_HOLIDAY_START_DATE")
        self.payload = {"queryYear": self.start_date.year, "response": "csv"}
        self.maxEntry = 0

    def start_requests(self):
        while self.maxEntry <= 5:
            try:
                r = requests.post(
                    self.url,
                    data=self.payload,
                )
                r = r.content.decode("big5")
                return r
            except requests.exceptions.RequestException as e:
                logger.error(self.url + " connection error")
                logger.error(e)
                logger.error("sleep 10 s")
                time.sleep(10)
                logger.error("try again")
                self.maxEntry += 1
                continue

    def parse(self, data):
        df = pd.read_csv(io.StringIO(data), skiprows=1)

        holiday_date = df["日期"]
        holiday_date = holiday_date.str.replace("月", "-")
        holiday_date = holiday_date.str.replace("日", "")
        holiday_date = str(self.start_date.year) + "-" + holiday_date
        holiday_date = pd.to_datetime(holiday_date).dt.date

        return holiday_date

    def save_data(self, holiday):

        for _holiday in holiday:
            try:
                row = Holiday.objects.create(date=_holiday)
                row.save()
                logger.info(f"{row.date} saved")
            except Exception as e:
                logger.error(f"Faild to insert date: {_holiday}")
                logger.error("Detail: " + str(e))

    def main(self):
        while self.start_date.year <= date.today().year:
            response = self.start_requests()
            data_parse = self.parse(response)
            self.save_data(data_parse)
            self.start_date += timedelta(days=365)
            setattr(config, "CRAWLER_HOLIDAY_START_DATE", self.start_date)
