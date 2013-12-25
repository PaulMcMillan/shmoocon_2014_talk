from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.results import dashboard


class Vnc(horizon.Panel):
    name = _("VNC")
    slug = "vnc"


dashboard.Results.register(Vnc)
