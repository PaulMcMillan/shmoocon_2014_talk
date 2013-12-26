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
        data = MasscanQueue().lrange()
        for i, datum in enumerate(data):
            d = datum._asdict()
            d['id'] = i
            result.append(d)
        return result
