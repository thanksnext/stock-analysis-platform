from celery import shared_task

from .crawler import StockCrawler


@shared_task
def start_crawler():
    crawler = StockCrawler()
    # crawler.crawl()
    crawler.main()
