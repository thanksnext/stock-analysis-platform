import logging
from datetime import datetime

from constance import config
from fundamentals.models import BalanceSheet, ComprehensiveIncome
from stock.models import Stock
from taiex.models import Taiex

logger = logging.getLogger("finance")


def run():
    model_info_list = [
        {
            "name": "taiex",
            "model": Taiex,
            "constance_config": "CRAWLER_TAIEX_START_DATE",
        },
        {
            "name": "stock",
            "model": Stock,
            "constance_config": "CRAWLER_STOCK_START_DATE",
        },
        {
            "name": "comprehensive_income",
            "model": ComprehensiveIncome,
            "constance_config": "CRAWLER_STOCK_START_DATE_COMPREHENSIVE",
        },
        {
            "name": "balance_sheet",
            "model": BalanceSheet,
            "constance_config": "CRAWLER_STOCK_START_DATE_BALANCE",
        },
    ]

    for model_info in model_info_list:
        try:
            latest_datetime = getattr(config, model_info["constance_config"])
            if type(latest_datetime) == str:
                latest_datetime = datetime.strptime(latest_datetime, "%Y-%m-%d").date()
                setattr(config, model_info["constance_config"], latest_datetime)
                logger.info(
                    f"Changed constance config type of {model_info['name']} from string to datetime successfully, type:{type(latest_datetime)}"
                )
            else:
                logger.debug(
                    f"Failed to change constance config type of {model_info['name']}, \
                    the reason may be because it was already in datetime format.\
                    type: {type(latest_datetime)}"
                )
                continue
        except Exception as e:
            logger.debug(e)
            logger.error(f"Failed to update latest date of {model_info['name']}")
