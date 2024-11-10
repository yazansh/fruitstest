# backend/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruitstest.settings')

app = Celery('fruitstest')

# Load task modules from all registered Django apps
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery Beat Schedule
app.conf.beat_schedule = {
    'say_hello_every_minute': {
        'task': 'offer.tasks.check_parcels',
        'schedule': crontab(minute='*/1'),  # Run every minute
    },
}