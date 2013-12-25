from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.tasks import dashboard


class Portscan(horizon.Panel):
    name = _("Portscan")
    slug = "portscan"


dashboard.Tasks.register(Portscan)
