import logging
import time

import pandas as pd
import requests

# from constance import config
from .models import Company, CompanyType

logger = logging.getLogger("finance")


class StockCompanyCrawler:
    def __init__(self):
        self.urlBase = "https://mops.twse.com.tw/mops/web/ajax_t51sb01"
        self.maxEntry = 0
        self.headers = {
            "Connection": "close",
        }

        self.payload = {
            "encodeURIComponent": 1,
            "step": 1,
            "firstin": 1,
            "off": 1,
            "TYPEK": "sii",
            "code": "",
        }

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

    def parse(self, data):

        read_data = pd.read_html(data.text, header=None)
        read_data_df = pd.concat(read_data, axis=0, sort=False)

        # 補齊欄位及固定欄位
        dtypes = ["object", "object", "object", "object"]
        fixAttr = ["公司代號", "公司名稱", "公司簡稱", "產業類別"]

        read_data_df = read_data_df[fixAttr]
        columns = list(read_data_df)
        columns_dtype = dict(zip(columns, dtypes))
        read_data_df = read_data_df.astype(columns_dtype)

        return read_data_df

    def crawl(self):

        response = self.start_requests()
        data_parse = self.parse(response)
        self.save_data(data_parse)

        return data_parse

    def save_data(self, data):

        for index, row in data.iterrows():
            if (
                row["公司代號"] == "公司代號"
                or row["公司名稱"] == "公司名稱"
                or row["公司簡稱"] == "公司簡稱"
                or row["產業類別"] == "產業類別"
            ):
                continue
            typeDetail = list(CompanyType.objects.filter(company_type=row["產業類別"]))
            if len(typeDetail) == 0:
                typeData = CompanyType.objects.create_ci(row["產業類別"])
                typeData.save()
                getType = list(CompanyType.objects.filter(company_type=row["產業類別"]))[0]
            else:
                getType = typeDetail[0]

            row = row.drop(labels=["產業類別"])
            row["company_type"] = getType.id
            company_type_obj = getType
            companyObj = {
                "company_name": row["公司名稱"],
                "company_abbreviation": row["公司簡稱"],
                "company_type_id": str(row["company_type"]),
            }
            companyDetail = list(Company.objects.filter(company_code=row["公司代號"]))

            if len(companyDetail) == 0:
                saveCompanyData = company_type_obj.company.create_ci(*row)
                saveCompanyData.save()
            else:
                Company.objects.filter(company_code=row["公司代號"]).update(**companyObj)
