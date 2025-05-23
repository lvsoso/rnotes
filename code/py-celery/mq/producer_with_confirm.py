# coding=utf-8
import sys
import pika

parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2F')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.confirm_delivery()

channel.exchange_declare(exchange='develop', exchange_type='direct',
                         passive=False, durable=True, auto_delete=False)
if len(sys.argv) != 1:
    msg = sys.argv[1]
else:
    msg = 'hah'

props = pika.BasicProperties(content_type='text/plain', delivery_mode=2)
if channel.basic_publish('develop', 'xxx_routing_key', msg,
                         properties=props):
    print('Message publish was confirmed!')
else:
    print('Message could not be confirmed!')
connection.close()
