import sys
import uuid
from kombu import Connection, Exchange, Queue

if len(sys.argv) > 1:
    uid = int(sys.argv[1])
else:
    uid = 0
print('uid = {}'.format(uid))

routing_key='user_{}'.format(uid)
print('routing key: {}'.format(routing_key))

exchange = Exchange(routing_key, 'fanout', durable=True, auto_delete=True)

# maybe i can use a temporary queue here
queue = Queue(str(uuid.uuid1()), exchange=exchange, routing_key=routing_key, exclusive=True, auto_delete=True)
