from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.tasks import dashboard


class Overview(horizon.Panel):
    name = _("Overview")
    slug = "overview"


dashboard.Tasks.register(Overview)
