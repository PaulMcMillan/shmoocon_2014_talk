from horizon import views
from horizon import tables

import tables as blacklist_tables

class IndexView(tables.DataTableView):
    table_class = blacklist_tables.BlacklistTable
    template_name = 'infrastructure/blacklist/index.html'

    def get_data(self):
        """ This is really hacky, but it fills out the table with
        _something_.
        """
        results = []
        line_id = 0
        try:
            with open('/etc/masscan/excludes.txt') as f:
                for line in f:
                    if line.strip():
                        line_id += 1
                        results.append({'value': line.strip(),
                                        'id': line_id})
        except IOError:
            pass
        return results
