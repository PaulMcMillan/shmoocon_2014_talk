from horizon import views
from horizon import tables

from tasa.store import connection

import tables as worker_tables


class IndexView(tables.DataTableView):
    table_class = worker_tables.WorkerTable
    template_name = 'infrastructure/workers/index.html'

    def get_data(self):
        result = connection.client_list()
        for client in result:
            client['address'], client['port'] = client['addr'].split(':')
        return result
