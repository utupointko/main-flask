import pika

params = pika.URLParameters('amqps://vaihkxgq:WNZrLPL6jg44KIhv0QEoEDk_ButDDPmb@cow.rmq2.cloudamqp.com/vaihkxgq')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Receiving in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
