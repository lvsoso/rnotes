### 启动

```shell
# 启动
celery -A main worker -l INFO
# 自动多进程
celery  multi start main -A main -l debug --autoscale=10,5
# 停止
ps auxww|grep "celery -A main worker"|grep -v grep|awk '{print $2}'|xargs kill -9 
# 查看
celery -A main  status 
```

### 调用
```shell
(base) 192:redis-celery wuqilv$ python
Python 3.11.9 (main, Apr 19 2024, 11:44:45) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import main
>>> t = main.add.delay(2,3)
>>> t.get()
5
>>> t.ready() #返回true证明可以执行，不必等待
True
>>> t.get(timeout=1) #如果1秒不返回结果就超时,避免一直等待
5
>>> t.get(propagate=False) #如果执行的代码错误只会打印错误信息
5
>>> t.traceback  #打印异常详细结果
```
