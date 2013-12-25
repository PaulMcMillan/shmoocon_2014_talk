from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.infrastructure import dashboard


class Workers(horizon.Panel):
    name = _("Workers")
    slug = "workers"


dashboard.Infrastructure.register(Workers)
