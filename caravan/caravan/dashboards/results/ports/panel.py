from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.results import dashboard


class Ports(horizon.Panel):
    name = _("Ports")
    slug = "ports"


dashboard.Results.register(Ports)
