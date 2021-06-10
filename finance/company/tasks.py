from celery import shared_task

from .crawler import StockCompanyCrawler


@shared_task
def start_company_crawler():
    crawler = StockCompanyCrawler()
    crawler.crawl()
