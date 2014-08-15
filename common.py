import sys
from kombu import Connection, Exchange, Queue, utils

if len(sys.argv) > 1:
    uid = int(sys.argv[1])
else:
    uid = 0
print('uid = {}'.format(uid))

exchange_name='user_{}'.format(uid)
print('exchange name: {}'.format(exchange_name))

exchange = Exchange(exchange_name, durable=True, auto_delete=True)

# maybe i can use a temporary queue here
queue = Queue(utils.uuid(), exchange=exchange, exclusive=True, auto_delete=True)
