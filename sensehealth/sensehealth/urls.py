from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from  sensehealth_api import urls as api_urls


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(api_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
