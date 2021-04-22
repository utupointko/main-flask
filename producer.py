import json
import pika

params = pika.URLParameters('amqps://vaihkxgq:WNZrLPL6jg44KIhv0QEoEDk_ButDDPmb@cow.rmq2.cloudamqp.com/vaihkxgq')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
