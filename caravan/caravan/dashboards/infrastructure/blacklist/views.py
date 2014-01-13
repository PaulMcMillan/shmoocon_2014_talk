from horizon import views
from horizon import tables

import tables as blacklist_tables

class IndexView(tables.DataTableView):
    table_class = blacklist_tables.BlacklistTable
    template_name = 'infrastructure/blacklist/index.html'

    def get_data(self):
        results = []
        try:
            with open('/etc/masscan/excludes.txt') as f:
                for line in f:
                    if line.strip():
                        results.append({'value': line.strip()})
        except IOError:
            pass
        return results
