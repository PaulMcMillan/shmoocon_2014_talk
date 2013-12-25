from horizon import tables

import tables as task_tables

class IndexView(tables.DataTableView):
    table_class = task_tables.TCPScanTable
    template_name = 'tasks/portscan/index.html'

    def get_data(self):
        return []
