import pika
import json


class EventPublisher:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("rabbitmq")
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="order_events")

    def publish(self, event_data):
        self.channel.basic_publish(
            exchange="",
            routing_key="order_events",
            body=json.dumps(event_data),
        )
