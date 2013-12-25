from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.tasks import dashboard


class Rdp(horizon.Panel):
    name = _("RDP")
    slug = "rdp"


dashboard.Tasks.register(Rdp)
