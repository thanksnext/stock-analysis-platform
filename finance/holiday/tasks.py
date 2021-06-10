from celery import shared_task

from .crawler import HolidayCrawler


@shared_task
def start_crawler():
    crawler = HolidayCrawler()
    # crawler.crawl()
    crawler.main()
