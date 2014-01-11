from horizon import views
from horizon import tables

import tables as worker_tables

class IndexView(tables.DataTableView):
    table_class = worker_tables.WorkerTable
    template_name = 'infrastructure/workers/index.html'

    def get_data(self):
        return []
