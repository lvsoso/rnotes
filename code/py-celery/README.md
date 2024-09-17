
### rabbitmq 

#### 启动
```shell
docker pull rabbitmq:management
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```

#### 访问

http://localhost:15672/

guest/guest




### celery

#### 组件
- billiard : 基于 Python2.7 的 multisuprocessing 而改进的库, 主要用来提高性能和稳定性.
- librabbitmp :C 语言实现的 Python 客户端
- kombu : Celery 自带的用来收发消息的库, 提供了符合 Python 语言习惯的, 使用 AMQP 协议的高级接口.


##### 配置
```python
task_reject_on_worker_lost = True    # 作用是当worker进程意外退出时，task会被放回到队列中
task_acks_late = True            # 作用是只有当worker完成了这个task时，任务才被标记为ack状态
visibility_timeout = 3600 # celery 在执行task时有个机制,就是任务时长超过了 visibility_timeout 时还没执行完,就会指定其他worker重新开始task,默认的时长是一小时
broker_transport_options = { 'visibility_timeout': 3600}
```

#### 注意

1. ETA 任务
> 对于  ETA 和 countdown 的任务，redis broker 会直接交给worker，由worker自己处理。如果还未处理，worker 发生重启，任务会丢失。
> 需要配置 task_acks_late 为 True，这样在未执行完成，任务不会被ack，会放到redis的一个unacked队列中。在超过 visibility_timeout 时间后，worker 将会再次尝试执行这个任务。



```shell
pip3 install celery[librabbitmq,redis,msgpack]
```

base

```shell
celery -A base.app  worker -l info
```

调用

```shell
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

### 例子

启动 redis-celery

```shell
(base) 192:redis-celery wuqilv$ cd redis-celery
(base) 192:redis-celery wuqilv$ celery -A main worker -l INFO  -Q queue_add,queue_task1,queue_task2,queue_task3
 
 -------------- celery@192.168.2.182 v5.4.0 (opalescent)
--- ***** ----- 
-- ******* ---- macOS-11.6.8-x86_64-i386-64bit 2024-09-17 15:18:19
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         mycelery:0x10f32dd60
- ** ---------- .> transport:   redis://localhost:6379/0
- ** ---------- .> results:     redis://localhost:6379/1
- *** --- * --- .> concurrency: 8 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> queue_add        exchange=queue_add(direct) key=queue_add
                .> queue_task1      exchange=queue_task1(direct) key=queue_task1
                .> queue_task2      exchange=queue_task2(direct) key=queue_task2
                .> queue_task3      exchange=queue_task3(direct) key=queue_task3

[tasks]
  . main.add
  . main.task1
  . main.task2
  . main.task3
```

signature 方式，可以将任务和参数打包传给另外的函数作为参数

```shell
(base) 192:redis-celery wuqilv$ python
Python 3.11.9 (main, Apr 19 2024, 11:44:45) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import main
>>> main.add.s(2,2)
main.add(2, 2)
>>> a = main.add.s(2,2)
>>> a.delay()
<AsyncResult: 8830112b-a2ba-4a91-ad41-1dba1acfa7cc>
```

group 方式，并行执行一组任务，并返回一组结果，可以按顺序获取结果

```shell
(base) 192:redis-celery wuqilv$ python
Python 3.11.9 (main, Apr 19 2024, 11:44:45) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import task1,task2,task3
>>> from celery import group
>>> my_group = group(task1.s(10,10), task2.s(20,20), task3.s(30,30))
>>> ret = my_group()
>>> print(ret.get())
[20, 40, 60]

# worker 显示
[2024-09-17 14:47:48,546: INFO/MainProcess] Task main.task1[fffafb88-9bde-4ee0-a35b-bd4d4f0b6f98] received
[2024-09-17 14:47:48,547: INFO/MainProcess] Task main.task2[8d199e47-51cc-4ba9-bfe0-c94b54b42b95] received
[2024-09-17 14:47:48,548: INFO/MainProcess] Task main.task3[27db1791-347a-4c7f-b253-f260e295e50b] received
[2024-09-17 14:47:48,548: WARNING/ForkPoolWorker-8] 任务函数 task1 正在执行...
[2024-09-17 14:47:48,550: WARNING/ForkPoolWorker-1] 任务函数 task2 正在执行...
[2024-09-17 14:47:48,551: WARNING/ForkPoolWorker-2] 任务函数 task3 正在执行...
[2024-09-17 14:47:48,562: INFO/ForkPoolWorker-8] Task main.task1[fffafb88-9bde-4ee0-a35b-bd4d4f0b6f98] succeeded in 0.01429122599074617s: 20
[2024-09-17 14:47:48,562: INFO/ForkPoolWorker-2] Task main.task3[27db1791-347a-4c7f-b253-f260e295e50b] succeeded in 0.011792852979851887s: 60
[2024-09-17 14:47:48,562: INFO/ForkPoolWorker-1] Task main.task2[8d199e47-51cc-4ba9-bfe0-c94b54b42b95] succeeded in 0.012568505015224218s: 40
```


chain 方式，任务一个一个执行，一个执行完并将结果传递给下一个任务函数

```shell
(base) 192:redis-celery wuqilv$ python
Python 3.11.9 (main, Apr 19 2024, 11:44:45) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import task1,task2,task3
>>> from celery import chain
>>> my_chain = chain(task1.s(10, 10)| task2.s(20) | task3.s(30))
>>> ret = my_chain()
>>> ret.get()
70
>>> 

# worker 显示
[2024-09-17 14:53:06,756: INFO/MainProcess] Task main.task1[c92cad25-bae1-4ab1-a9fd-8cf0ce7e813c] received
[2024-09-17 14:53:06,758: WARNING/ForkPoolWorker-8] 任务函数 task1 正在执行...
[2024-09-17 14:53:06,774: INFO/MainProcess] Task main.task2[d3f6a8cb-e5e2-4256-a46a-776b85602173] received
[2024-09-17 14:53:06,774: INFO/ForkPoolWorker-8] Task main.task1[c92cad25-bae1-4ab1-a9fd-8cf0ce7e813c] succeeded in 0.01637955298065208s: 20
[2024-09-17 14:53:06,776: WARNING/ForkPoolWorker-1] 任务函数 task2 正在执行...
[2024-09-17 14:53:06,788: INFO/MainProcess] Task main.task3[26264fe6-0776-4695-92d9-f506ec7c807b] received
[2024-09-17 14:53:06,789: INFO/ForkPoolWorker-1] Task main.task2[d3f6a8cb-e5e2-4256-a46a-776b85602173] succeeded in 0.013115486013703048s: 40
[2024-09-17 14:53:06,789: WARNING/ForkPoolWorker-8] 任务函数 task3 正在执行...
[2024-09-17 14:53:06,790: INFO/ForkPoolWorker-8] Task main.task3[26264fe6-0776-4695-92d9-f506ec7c807b] succeeded in 0.0012587889796122909s: 70
```



##### 参考


https://github.com/celery/celery/issues/7651
https://juejin.cn/post/7011163709238149128



