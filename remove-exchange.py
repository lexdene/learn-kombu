from kombu import Connection

import config, common

with Connection(config.AMQP_URL) as conn:
    exchange = common.exchange(conn.channel())
    exchange.delete()

    queue = common.queue(conn.channel())
    queue.delete()
