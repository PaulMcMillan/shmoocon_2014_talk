from horizon import tables

class TCPScanTable(tables.DataTable):
    seed = tables.Column('seed')
    shards = tables.Column('shard')
    ports = tables.Column('ports')

    class Meta:
        name = 'tcp_scan'
        verbose_name = 'Portscan'
