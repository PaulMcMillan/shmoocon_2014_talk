from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.infrastructure import dashboard


class Vm(horizon.Panel):
    name = _("Virtual")
    slug = "vm"


dashboard.Infrastructure.register(Vm)
