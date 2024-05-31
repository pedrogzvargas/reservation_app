import os
import json
from kombu import Connection
from kombu import Exchange
from kombu import Queue
from kombu.mixins import ConsumerMixin
from dotenv import load_dotenv
from modules.shared.infraestructure.message_handler import message_handler

load_dotenv()
rabbit_url = os.getenv('RABBITMQ_URL')


class Consumer(ConsumerMixin):
    def __init__(self, connection, queues):
        self.connection = connection
        self.queues = queues

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=self.queues, callbacks=[self.on_message])]

    def on_message(self, body, message):
        if isinstance(body, str):
            body = json.loads(body)
        event_name = body.get("event_name")
        handler = message_handler.get(event_name)
        if not handler:
            message.ack()
        handler = handler(message=message)
        handler(body=body)


if __name__ == "__main__":
    exchange = Exchange("traxion-exchange", type="direct")
    queues = [Queue("traxion-queue", exchange, routing_key="traxion")]

    with Connection(rabbit_url, heartbeat=4) as conn:
        worker = Consumer(conn, queues)
        worker.run()
