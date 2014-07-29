import datetime
from kombu import Connection, Exchange, Queue

import config, common

def process_data(body, message):
    print(body)
    message.ack()

with Connection(config.AMQP_URL) as conn:
    producer = conn.Producer(serializer='json')
    producer.publish(
        {
            'name': 'xxx',
            'datetime': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        },
        exchange=common.exchange,
        declare=[common.queue]
    )
