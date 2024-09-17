import pika


def on_message(channel, method_frame, header_frame, body):
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    print(body)

parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2F')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='develop', exchange_type='direct',
                         passive=False, durable=True, auto_delete=False)

channel.queue_declare(queue='standard', auto_delete=True)

channel.queue_bind(queue='standard', exchange='develop',
                   routing_key='xxx_routing_key')

channel.basic_consume('standard', on_message)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
