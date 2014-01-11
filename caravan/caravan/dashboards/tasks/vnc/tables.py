from horizon import tables

from looksee.workers import RFBPrintWorker, RFBScreenshotWorker


class DeletePrintJobs(tables.Action):
    name = 'delete'
    verbose_name = 'Delete Task'
    data_type_singular = 'Queue'
    action_present = "delete"
    requires_input = False
    preempt = True
    classes = ("btn-danger", "btn-delete")

    def handle(self, data_table, request, object_ids):
        MasscanQueue().clear()



class RFBPrintTable(tables.DataTable):
    ip = tables.Column('ip',
                       attrs={'data-type': "ip"})
    port = tables.Column('port')

    def get_object_id(self, datum):
        return datum.ip

    class Meta:
        name = 'rfb_print'
        verbose_name = 'Fingerprint'
        multi_select = False
        table_actions = (DeletePrintJobs,)


class DeleteScreenshotJobs(tables.Action):
    name = 'delete'
    verbose_name = 'Delete Task'
    data_type_singular = 'Queue'
    action_present = "delete"
    requires_input = False
    preempt = True
    classes = ("btn-danger", "btn-delete")

    def handle(self, data_table, request, object_ids):
        MasscanQueue().clear()



class RFBScreenshotTable(tables.DataTable):
    ip = tables.Column('ip',
                       verbose_name='IP Address',
                       attrs={'data-type': "ip"})
    port = tables.Column('port')

    def get_object_id(self, datum):
        return datum.ip

    class Meta:
        name = 'rfb_shot'
        verbose_name = 'Screenshot'
        multi_select = False
        table_actions = (DeleteScreenshotJobs,)
