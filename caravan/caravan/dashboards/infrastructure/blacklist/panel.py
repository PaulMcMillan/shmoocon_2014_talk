from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.infrastructure import dashboard


class Blacklist(horizon.Panel):
    name = _("Blacklist")
    slug = "blacklist"


dashboard.Infrastructure.register(Blacklist)
