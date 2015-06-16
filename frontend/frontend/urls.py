from django.conf.urls import patterns, include, url

from django.contrib import admin

#admin.autodiscover()

urlpatterns = [
    # Examples:

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]
