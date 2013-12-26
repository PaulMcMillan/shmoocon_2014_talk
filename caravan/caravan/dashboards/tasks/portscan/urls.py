from django.conf.urls.defaults import patterns  # noqa
from django.conf.urls.defaults import url  # noqa

from .views import IndexView, CreateView


urlpatterns = patterns('',
    url(r'^create/$', CreateView.as_view(), name='create'),
    url(r'^$', IndexView.as_view(), name='index'),
)
