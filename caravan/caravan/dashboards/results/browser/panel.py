from django.utils.translation import ugettext_lazy as _

import horizon

from caravan.dashboards.results import dashboard


class Browser(horizon.Panel):
    name = _("Browser")
    slug = "browser"


dashboard.Results.register(Browser)
