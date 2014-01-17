from horizon import views
from horizon import tables

from caravan.dashboards.tasks.vnc.tables import RFBPrintTable
from caravan.dashboards.tasks.vnc.tables import RFBScreenshotTable

from looksee.workers import RFBPrintWorker, RFBScreenshotWorker


class IndexView(tables.MultiTableView):
    table_classes = (RFBPrintTable, RFBScreenshotTable)
    # A very simple class-based view...
    template_name = 'tasks/vnc/index.html'

    def get_rfb_print_data(self):
        marker = int(self.request.GET.get(
                self.table_classes[0]._meta.pagination_param, 0))
        return RFBPrintWorker.qinput.id_and_chunk(marker)

    def get_rfb_shot_data(self):
        marker = int(self.request.GET.get(
                self.table_classes[1]._meta.pagination_param, 0))
        return RFBScreenshotWorker.qinput.id_and_chunk(marker)

    def has_more_data(self, table):
        # Yeah, I should fix this
        return True

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
