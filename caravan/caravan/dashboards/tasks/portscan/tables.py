from horizon import tables


class CreateScan(tables.LinkAction):
    name = 'create'
    verbose_name = 'New Scan'
    url = 'horizon:tasks:portscan:create'
    classes = ('ajax-modal', 'btn-create')


class TCPScanTable(tables.DataTable):
    iprange = tables.Column('iprange')
    ports = tables.Column('ports')
    proto = tables.Column('proto')
    shards = tables.Column('shards')
    seed = tables.Column('seed')
    qoutput = tables.Column('qoutput')

    def get_object_id(self, datum):
        return datum['id']

    class Meta:
        name = 'tcp_scan'
        verbose_name = 'Job Queue'
        table_actions = (CreateScan,)
