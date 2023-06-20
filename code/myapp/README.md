```shell
poetry env info

pip install fastapi "uvicorn[standard]"
pip wheel --use-pep517 "psycopg2 (==2.9.6)"


```

```shell
alembic revision --autogenerate -m 'add_user_table'
alembic upgrade head
```


```shell
cd app && uvicorn main:app --reload --port=8080 --host=0.0.0.0
```