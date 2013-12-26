from horizon import tables


from looksee.queues import MasscanQueue


class CreateScan(tables.LinkAction):
    name = 'create'
    verbose_name = 'New Scan'
    url = 'horizon:tasks:portscan:create'
    classes = ('ajax-modal', 'btn-create')


class DeleteScan(tables.Action):
    name = 'delete'
    verbose_name = 'Delete Task'
    data_type_singular = 'Queue'
    action_present = "delete"
    requires_input = False
    preempt = True
    classes = ("btn-danger", "btn-delete")

    def handle(self, data_table, request, object_ids):
        MasscanQueue().delete()


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
        table_actions = (CreateScan,DeleteScan)
        multi_select = False
