# from collections import OrderedDict
from datetime import date

CONSTANCE_CONFIG = {
    "CRAWLER_MIN_INTERVAL": (7, "Crawler minimum interval", int),
    "CRAWLER_MAX_INTERVAL": (9, "Crawler maximum interval", int),
    "CRAWLER_TAIEX_START_DATE": (
        date(1999, 1, 5),
        "Crawler start date for Taiex",
        date,
    ),
    "CRAWLER_STOCK_START_DATE": (
        date(2013, 1, 1),
        "crawler stock start date",
        date,
    ),
    "CRAWLER_STOCK_START_DATE_COMPREHENSIVE": (
        date(2013, 1, 1),
        "crawler stock start date for comprehensive",
        date,
    ),
    "CRAWLER_STOCK_START_DATE_BALANCE": (
        date(2013, 1, 1),
        "crawler stock start date for balance",
        date,
    ),
    "CRAWLER_HOLIDAY_START_DATE": (
        date(2021, 1, 1),
        "crawler stock start date for holiday",
        date,
    ),
}

CONSTANCE_CONFIG_FIELDSETS = {
    "Crawler Configs": (
        "CRAWLER_MIN_INTERVAL",
        "CRAWLER_MAX_INTERVAL",
        "CRAWLER_TAIEX_START_DATE",
        "CRAWLER_STOCK_START_DATE",
        "CRAWLER_STOCK_START_DATE_COMPREHENSIVE",
        "CRAWLER_STOCK_START_DATE_BALANCE",
        "CRAWLER_HOLIDAY_START_DATE",
    )
}
