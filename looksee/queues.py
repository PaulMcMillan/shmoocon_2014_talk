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
        return MasscanJob(*json.loads(value))

    def lrange(self, start=0, stop=-1):
        return (self.deserialize(item) for item in self.redis.lrange(self.name, 0, -1))


class ScanResultQueue(store.Queue):
    def deserialize(self, value):
        result = ScanResultQueue(json.loads(value))
        result.port = int(result.port)
        return result
