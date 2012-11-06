from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('supercomputer.urls')),
    url(r'^', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rosetta/', include('rosetta.urls')),
    #url(r'^i18n/', include('django.conf.urls.i18n')),
)
