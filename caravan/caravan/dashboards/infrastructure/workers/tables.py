from horizon import tables

from tasa.store import connection


class RestartWorker(tables.Action):
    name = 'restart'
    verbose_name = 'Restart Worker'
    data_type_singular = 'Worker'
    action_present = 'restart'
    requires_input = False
    classes = ('btn-warning',)

    def handle(self, data_table, request, object_ids):
        # Send a restart signal
        connection.publish('control', 'restart')


class WorkerTable(tables.DataTable):
    addr = tables.Column('address', verbose_name='Address')
    port = tables.Column('port')
    age = tables.Column('age')
    idle = tables.Column('idle')
    flags = tables.Column('flags')
    cmd = tables.Column('cmd', verbose_name='Last Command')

    def get_object_id(self, datum):
        return datum['addr']

    class Meta:
        name = 'workers'
        verbose_name = 'Connections'
        table_actions = (RestartWorker,)
        multi_select = False
