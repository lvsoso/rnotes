#!/usr/bin/env bash

gunicorn -w 4 -k gevent -b 127.0.0.1:5000 --log-level=debug main:app