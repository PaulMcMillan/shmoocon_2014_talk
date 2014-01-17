import json
from collections import namedtuple

from tasa import store


MasscanJob = namedtuple('MasscanJob',
                        ['iprange', 'ports', 'proto',
                         'shards', 'seed', 'qoutput'])


ScanResultJob = namedtuple('ScanResultJob',
                           ['port', 'ip'])


class LookseeQueue(store.Queue):
    blocking = 0

    def id_and_chunk(self, marker=0, size=99):
        result = []
        data = self[marker:marker + size]
        for i, datum in enumerate(data):
            d = datum._asdict()
            d['id'] = i + marker + 1
            result.append(d)
        return result



class MasscanQueue(LookseeQueue):
    """ Masscan parameter queue """
    name = 'masscan'

    def serialize(self, value):
        return json.dumps(map(str, value))

    def deserialize(self, value):
        if value:
            return MasscanJob(*json.loads(value))


class ScanResultQueue(LookseeQueue):
    def deserialize(self, value):
        if value:
            res = ScanResultJob(*json.loads(value))
            return res._replace(port=int(res.port))
