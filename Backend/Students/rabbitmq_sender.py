import pika
import json

class RabbitMQSender:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='lesson_queue')

    def send_to_queue(self, message):
        self.channel.basic_publish(exchange='',
                                    routing_key='lesson_queue',
                                    body=json.dumps(message))
        print(" [x] Sent %r" % message)

    def close_connection(self):
        self.connection.close()
