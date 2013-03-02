from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.defaults import *
from main.views import *
from django.conf.urls.defaults import *
admin.autodiscover()

# And include this URLpattern...
urlpatterns = patterns('',
    ('^$', index),
    (r'^submit/', submit),
    (r'^latest/', latest),
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/opt/shoot/static'}),
)
