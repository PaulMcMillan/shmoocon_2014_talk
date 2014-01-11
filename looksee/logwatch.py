import json
from pprint import pprint

from tasa.store import connection

pubsub = connection.pubsub()
pubsub.subscribe('logging')
try:
    for message in pubsub.listen():
        if message['type'] == 'message':
            pprint(json.loads(message['data']))
except KeyboardInterrupt:
    pass
