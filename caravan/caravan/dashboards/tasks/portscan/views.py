from django.core.urlresolvers import reverse_lazy

from horizon import tables
from horizon import forms

import tables as scan_tables
import forms as scan_forms

import tasa.store
from looksee.queues import MasscanQueue

class CreateView(forms.ModalFormView):
    form_class = scan_forms.CreateScan
    template_name = 'tasks/portscan/create.html'
    success_url = reverse_lazy('horizon:tasks:portscan:index')


class IndexView(tables.DataTableView):
    table_class = scan_tables.TCPScanTable
    template_name = 'tasks/portscan/index.html'

    def get_data(self):
        result = []
        marker = int(self.request.GET.get(
                self.table_class._meta.pagination_param, 0))
        return MasscanQueue().id_and_chunk(marker)

    def has_more_data(self, table):
        if len(MasscanQueue()) > 0:
            return True
        else:
            return False
