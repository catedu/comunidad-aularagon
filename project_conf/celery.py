"""
Celery config file

https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

"""

from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
environment = (
    "dev" if os.environ.get("SETTINGS_SELECTION") in ["dev", None] else "production"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"project_conf.settings.{environment}")

# you change change the name here
app = Celery("project_conf")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# app.conf.beat_schedule = {
#     "count_hompage_3s": {"task": "home.tasks.count_hompage", "schedule": 3.0}
# }


@app.task
def add(x, y):
    return x / y