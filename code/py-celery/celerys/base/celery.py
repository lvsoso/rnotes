from __future__ import absolute_import

from celery import Celery

app = Celery('base', include=['base.tasks'])
app.config_from_object('base.celeryconfig')


if __name__ == '__main__':
    app.start()
