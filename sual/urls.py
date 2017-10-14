from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from profiles import views


api_urls = [
    url(r'^users/', include('profiles.urls', namespace='users')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]
