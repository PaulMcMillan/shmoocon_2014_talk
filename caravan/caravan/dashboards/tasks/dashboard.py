from django.utils.translation import ugettext_lazy as _

import horizon


class Tasks(horizon.Dashboard):
    name = _("Tasks")
    slug = "tasks"
    panels = ('overview', 'portscan', 'vnc', 'rdp', 'browser')  # Add your panels here.
    default_panel = 'overview'  # Specify the slug of the dashboard's default panel.


horizon.register(Tasks)
