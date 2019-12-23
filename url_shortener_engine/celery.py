from __future__ import absolute_import

import os
import warnings

from django.conf import settings

from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings.dev")

app = Celery("url_shortener")
app.conf.broker_url = "redis://redis:6379/0"
app.conf.result_backend = "redis://redis:6379/1"
app.config_from_object("django.conf:settings")
app.conf.imports = (
    'url_shortener.tasks',
)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.task_acks_late = "Enabled"
warnings.filterwarnings("ignore")

app.conf.beat_schedule = {
    'delete_outdate_url': {
         'task': 'delete_outdate_url',
         'schedule': crontab(minute=0, hour=0),
     },
}
app.conf.timezone = 'Europe/London'
app.conf.enable_utc = True


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request), flush=True)