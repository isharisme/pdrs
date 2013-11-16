from django.conf.urls import patterns, include, url

from website import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdrs.views.home', name='home'),
    # url(r'^pdrs/', include('pdrs.foo.urls')),
    url(r'^website/', include('website.urls', namespace="website")),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
