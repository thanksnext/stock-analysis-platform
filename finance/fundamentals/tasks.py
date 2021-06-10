from celery import shared_task

from .crawler import BalanceSheetAndIncomeStatementCrawler


@shared_task
def start_fundamentals_crawler(paramObj):
    crawler = BalanceSheetAndIncomeStatementCrawler(paramObj)
    crawler.crawl()
