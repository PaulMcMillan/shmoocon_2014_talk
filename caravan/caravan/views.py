from django import shortcuts
from django.views.decorators import vary


import horizon


@vary.vary_on_cookie
def splash(request):
    return shortcuts.redirect(horizon.get_dashboard('tasks').get_absolute_url())
