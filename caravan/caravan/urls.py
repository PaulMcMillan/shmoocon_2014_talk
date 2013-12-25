from django.conf.urls import patterns, include, url

from django.conf import settings  # noqa
from django.conf.urls.static import static  # noqa
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # noqa


import horizon

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'caravan.views.splash', name='splash'),
    url(r'^auth/login', 'django.contrib.auth.views.login', name='login'),
    url(r'^auth/logout', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(horizon.urls)),
)


# Development static app and project media serving using the staticfiles app.
urlpatterns += staticfiles_urlpatterns()

# Convenience function for serving user-uploaded media during
# development. Only active if DEBUG==True and the URL prefix is a local
# path. Production media should NOT be served by Django.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^500/$', 'django.views.defaults.server_error')
    )
