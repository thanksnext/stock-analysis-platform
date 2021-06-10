from __future__ import absolute_import, unicode_literals

import os
from pathlib import Path

import environ
from celery import Celery
from celery.signals import setup_logging

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_PACKAGE = Path(__file__).resolve(strict=True).parent
print(PROJECT_PACKAGE)
BASE_DIR = PROJECT_PACKAGE.parent
env.read_env(os.path.join(BASE_DIR, "envfile"))
BROKER_URL = env.str("BROKER_URL", default="")

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finance.settings.settings")

# BROKER_URL = "amqp://guest:guest@rabbitmq:5672/vhost"

app = Celery("finance", broker=BROKER_URL)


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("finance.settings.celery_config")

# Load task modules from all registered Django app configs.
# 撈出所有app下的task
app.autodiscover_tasks()


@setup_logging.connect
def config_loggers(*args, **kwags):
    from logging.config import dictConfig

    from finance.settings import settings

    dictConfig(settings.LOGGING)


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
