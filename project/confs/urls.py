"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from project.settings import base

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Static files, served from server
    url(r'^static/(\?P.*)$', 'django.views.static.serve', {'document_root': base.STATIC_ROOT}),

    # url(r'^', include('apps.public.urls')),
    url(r'^$', TemplateView.as_view(template_name='base.html')),
)