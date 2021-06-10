from celery import shared_task

from .crawler import TaiexCrawler


@shared_task
def start_crawler():
    crawler = TaiexCrawler()
    crawler.crawl()
