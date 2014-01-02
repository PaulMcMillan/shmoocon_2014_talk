import json
from collections import namedtuple

from tasa import store


MasscanJob = namedtuple('MasscanJob',
                        ['iprange', 'ports', 'proto',
                         'shards', 'seed', 'qoutput'])

ScanResultJob = namedtuple('ScanResultJob',
                           ['port', 'ip'])


class MasscanQueue(store.Queue):
    """ Masscan parameter queue """
    name = 'masscan'

    def serialize(self, value):
        return json.dumps(map(str, value))

    def deserialize(self, value):
        if value:
            return MasscanJob(*json.loads(value))


class ScanResultQueue(store.Queue):
    def serialize(self, value):
        value[0] = int(value[0])
        return json.dumps(value)

    def deserialize(self, value):
        if value:
            return ScanResultJob(*json.loads(value))
