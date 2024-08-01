# coding=utf-8
from datetime import timedelta

# BROKER_URL = 'amqp://guest:guest@localhost:5672/%2F'
BROKER_URL =  'redis://localhost:36379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:36379/0'
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

CELERYBEAT_SCHEDULE = {
    'add': {
        'task': 'beat.tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    }
}

CELERY_SEND_TASK_SENT_EVENT = True
