#!/usr/bin/env python
import pika
import time
import os

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# url = os.environ.get('CLOUDAMQP_URL', 'amqps://ekrrafvx:6DZsd-zG_NvZqZDbrQDIlhR0MKV8b3uP@gull.rmq.cloudamqp.com/ekrrafvx')
# params = pika.URLParameters(url)
# connection = pika.BlockingConnection(params)
# channel = connection.channel()

channel.queue_declare(queue='IoTEquipo8Carlos', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='IoTEquipo8Carlos', on_message_callback=callback)

channel.start_consuming()
