from celery.schedules import crontab

beat_scheduler = "django_celery_beat.schedulers.DatabaseScheduler"
accept_content = ["json"]
task_serializer = "json"
result_serializer = "json"
timezone = "Asia/Taipei"
enable_utc = True

beat_schedule = {
    "company-crawler": {
        # company.tasks
        "task": "company.tasks.start_company_crawler",
        "schedule": crontab(minute="*/10"),
    },
    "holiday-crawler": {
        # holiday.tasks
        "task": "holiday.tasks.start_crawler",
        "schedule": crontab(minute="*/10"),
    },
    "income-crawler": {
        # fundamentals.tasks
        "task": "fundamentals.tasks.start_fundamentals_crawler",
        "schedule": crontab(minute="*/10"),
        "args": ["Income"],
    },
    "balance-crawler": {
        # fundamentals.tasks
        "task": "fundamentals.tasks.start_fundamentals_crawler",
        "schedule": crontab(minute="*/10"),
        "args": ["Balance"],
    },
    "taiex-crawler": {
        # taiex.tasks
        "task": "taiex.tasks.start_crawler",
        "schedule": crontab(minute="*/10"),
    },
    "stock-crawler": {
        # taiex.tasks
        "task": "stock.tasks.start_crawler",
        "schedule": crontab(minute="*/10"),
    },
}
