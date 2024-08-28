# coding=utf-8
from __future__ import absolute_import

from celery import Celery

app = Celery('spec_queues', include=['spec_queues.tasks'])
app.config_from_object('spec_queues.celeryconfig')


if __name__ == '__main__':
    app.start()
