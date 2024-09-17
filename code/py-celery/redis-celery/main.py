from celery import Celery

app = Celery(
    'mycelery',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1',
    broker_connection_retry_on_startup=True,
    broker_connection_max_retries=10,
    task_routes={
        'main.add' : {'queue': 'queue_add'},
        'main.task1' : {'queue': 'queue_task1'},
        'main.task2' : {'queue': 'queue_task2'},
        'main.task3' : {'queue': 'queue_task3'},
    })

@app.task
def add(x, y):  
    return x + y


@app.task
def task1(x,y):
    print('任务函数 task1 正在执行...')
    return x + y

@app.task
def task2(x,y):
    print('任务函数 task2 正在执行...')
    return x + y

@app.task
def task3(x,y):
    print('任务函数 task3 正在执行...')
    return x + y

