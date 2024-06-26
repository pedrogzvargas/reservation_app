import os
import json
import pathlib
import sys
from kombu import Connection
from kombu import Exchange
from kombu import Queue
from kombu.mixins import ConsumerMixin
from dotenv import load_dotenv


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = str(pathlib.Path(CURRENT_PATH).parent)
sys.path.append(os.path.join(PROJECT_PATH))

load_dotenv()
rabbit_url = os.getenv('RABBITMQ_URL')

from modules.shared.infraestructure.message_handler import message_handler


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
            return
        handler = handler(message=message)
        handler(body=body)


if __name__ == "__main__":
    xchange_name = os.getenv('RABBITMQ_EXCHANGE_NAME')
    exchange_type = os.getenv('RABBITMQ_EXCHANGE_TYPE')
    routing_key = os.getenv('RABBITMQ_ROUTING_KEY')
    queue_name = os.getenv('RABBITMQ_LISTENING_QUEUE_NAME')

    exchange = Exchange(xchange_name, type=exchange_type)
    queues = [Queue(queue_name, exchange, routing_key=routing_key)]

    with Connection(rabbit_url, heartbeat=4) as conn:
        worker = Consumer(conn, queues)
        worker.run()
