from django.utils.translation import ugettext_lazy as _

import horizon


class MachinePanels(horizon.PanelGroup):
    name = 'Machines'
    slug = 'machines'
    panels = ('vm', 'dedicated')


class ConfigPanels(horizon.PanelGroup):
    name = 'Configuration'
    slug = 'configuration'
    panels = ('workers', 'blacklist')


class MetricsPanels(horizon.PanelGroup):
    name = 'Metrics'
    slug = 'metrics'
    panels = ('bandwidth',)


class Infrastructure(horizon.Dashboard):
    name = _("Infra")
    slug = "infrastructure"
    panels = (MachinePanels, ConfigPanels, MetricsPanels)
    default_panel = 'bandwidth'


horizon.register(Infrastructure)
