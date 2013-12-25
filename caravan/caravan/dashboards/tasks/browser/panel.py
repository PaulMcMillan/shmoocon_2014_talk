from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.tasks import dashboard


class Browser(horizon.Panel):
    name = _("Browser")
    slug = "browser"


dashboard.Tasks.register(Browser)
