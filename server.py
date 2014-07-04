from kombu import Connection, Exchange, Queue

import config, common

def process_data(body, message):
    print(body)
    message.ack()

with Connection(config.AMQP_URL) as conn:
    with conn.Consumer(common.queue, callbacks=[process_data]) as consumer:
        print('connect success')
        while True:
            try:
                conn.drain_events()
            except KeyboardInterrupt:
                break

print('exit safely')
