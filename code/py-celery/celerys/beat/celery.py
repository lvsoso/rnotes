# coding=utf-8
from __future__ import absolute_import

from celery import Celery

app = Celery('beat', include=['beat.tasks'])
app.config_from_object('beat.celeryconfig')


if __name__ == '__main__':
    app.start()
