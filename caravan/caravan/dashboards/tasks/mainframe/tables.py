from horizon import tables

from looksee.workers import MainframeWorker


class DeleteScan(tables.Action):
    name = 'delete'
    verbose_name = 'Delete Task'
    data_type_singular = 'Queue'
    action_present = "delete"
    requires_input = False
    preempt = True
    classes = ("btn-danger", "btn-delete")

    def handle(self, data_table, request, object_ids):
        MainframeWorker().clear()


class MainframeScanTable(tables.DataTable):
    ip = tables.Column('ip')
    port = tables.Column('port')

    def get_object_id(self, datum):
        return datum['id']

    class Meta:
        name = 'mainframe_scan'
        verbose_name = 'Mainframe Scan Queue'
        table_actions = (DeleteScan,)
        multi_select = False
