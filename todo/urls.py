from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'todo.views.list', name='list'),
    url(r'^new/?$', 'todo.views.create', name='create'),
    url(r'^admin/', include(admin.site.urls)),
)
