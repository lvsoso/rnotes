
### rabbitmq 启动
```shell
docker pull rabbitmq:management
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```

### 访问

http://localhost:15672/

guest/guest


### celery

```shell
pip3 install celery[librabbitmq,redis,msgpack]
```

base

```shell
celery -A base.app  worker -l info

(base) 192:celerys wuqilv$ python3
Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from base.tasks import add
>>> r = add.delay(1,3)
>>> r
<AsyncResult: 3f7a94e4-2e42-45d8-bb16-1f8e8df6d484>
>>> r.result
4
>>> r.status
'SUCCESS'
>>> r.successful()
True
>>> r.backend
<celery.backends.redis.RedisBackend object at 0x11187c770>
>>> task_id='3f7a94e4-2e42-45d8-bb16-1f8e8df6d484'
>>> add.AsyncResult(task_id).get()
4
```

queue

```shell
celerys wuqilv$ celery -A spec_queues worker -Q web_tasks -l info
```

beat

```shell
celery -A beat beat

celery -A beat worker -l info


>>> from datetime import datetime, timedelta
>>> from zoneinfo import ZoneInfo
>>> run_time = datetime(2024, 8, 2, 5, 26, 00, tzinfo=ZoneInfo("Asia/Shanghai"))
>>> add.apply_async(args=[1, 10 ], eta=run_time2)
<AsyncResult: ffed43a3-833f-4f28-8278-9d41aeebaba2>
```

celery-socketio

```shell
python3 celery_socketio.py

celery -A celery_socketio.celery -P eventlet worker -l info
```