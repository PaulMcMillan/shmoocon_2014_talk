from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.infrastructure import dashboard


class Bandwidth(horizon.Panel):
    name = _("Bandwidth")
    slug = "bandwidth"


dashboard.Infrastructure.register(Bandwidth)
