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
        return RFBPrintWorker.qinput[:]

    def get_rfb_shot_data(self):
        return RFBScreenshotWorker.qinput[:]

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
