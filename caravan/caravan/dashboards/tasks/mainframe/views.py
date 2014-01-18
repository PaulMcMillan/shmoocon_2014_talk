from horizon import views
from horizon import tables

import tables as mainframe_tables

from looksee.workers import MainframeWorker


class IndexView(tables.DataTableView):
    table_class = mainframe_tables.MainframeScanTable
    template_name = 'tasks/mainframe/index.html'

    def get_data(self):
        result = []
        marker = int(self.request.GET.get(
                self.table_class._meta.pagination_param, 1))
        return MainframeWorker.qinput.id_and_chunk(marker)

    def has_more_data(self, table):
        if len(MainframeWorker.qinput) > 0:
            return True
        else:
            return False
