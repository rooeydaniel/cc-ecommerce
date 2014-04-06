"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('apps.public',
    url(r'^my_account$', 'views.edit_user', name="edit_user"),
    url(r'^create_user$', 'views.create_user', name="create_user"),
    url(r'^logout$', 'views.logout', name="user_logout"),
    url(r'^login$', 'views.login', name="user_login"),
    url(r'^$', 'views.home', name="home"),
)