from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.tasks import dashboard


class Vnc(horizon.Panel):
    name = _("VNC")
    slug = "vnc"


dashboard.Tasks.register(Vnc)
