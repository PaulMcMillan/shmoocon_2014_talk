from django.utils.translation import ugettext_lazy as _

import horizon


class Results(horizon.Dashboard):
    name = _("Results")
    slug = "results"
    panels = ('browser', 'vnc', 'rdp', 'ports')  # Add your panels here.
    default_panel = 'vnc'  # Specify the slug of the dashboard's default panel.


horizon.register(Results)
