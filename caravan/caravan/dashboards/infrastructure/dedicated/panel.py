from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.infrastructure import dashboard


class Dedicated(horizon.Panel):
    name = _("Dedicated")
    slug = "dedicated"


dashboard.Infrastructure.register(Dedicated)
