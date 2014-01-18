from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.tasks import dashboard


class Mainframe(horizon.Panel):
    name = _("Mainframe")
    slug = "mainframe"


dashboard.Tasks.register(Mainframe)
