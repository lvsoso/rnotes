```shell
tar -xf redis-6.2.14.tar.gz
mkdir 7001 7002 7003 7004 7005 7006 redis-data run

redis-cli -a 123456 --cluster create 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 127.0.0.1:7006 --cluster-replicas 1

redis-cli -p 7617 -a "123456"
```