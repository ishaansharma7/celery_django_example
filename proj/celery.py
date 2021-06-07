from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab 
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='')

# app.conf.beat_schedule = {
#     'every-15-seconds':{
#         'task':'app2email.tasks.periodic_mail',
#         'schedule':crontab(minute=11, hour=12),
#         # 'schedule':15,
#     }
# }


# CELERY_BEAT_SCHEDULE = {
#     'every-15-seconds':{
#         'task':'app2email.tasks.periodic_mail',
#         # 'schedule':crontab(minute=0, hour=0),
#         'schedule':15,
#     }
# }
# Load task modules from all registered Django apps.
app.autodiscover_tasks()