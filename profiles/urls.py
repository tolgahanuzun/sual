from django.conf.urls import url
from profiles.views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, UserGetAPI, TokenUsers

urlpatterns = [
    url(r'^$', UserRegistrationAPIView.as_view(), name="list"),
    url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
    url(r'^logout/$', UserLogoutAPIView.as_view(), name="logout"),
    url(r'^token/$', TokenUsers.as_view()),
    url(r'^(?P<username>[-\w]+)/$', UserGetAPI.as_view()),
]