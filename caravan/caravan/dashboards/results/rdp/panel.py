from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.results import dashboard


class Rdp(horizon.Panel):
    name = _("RDP")
    slug = "rdp"


dashboard.Results.register(Rdp)
