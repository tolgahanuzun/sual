from django.conf.urls import url
from uptopic.views import TopicListAPIView, VoteCreateListAPIView, TopicGetListAPIView, TopicSourceListAPIView

urlpatterns = [
    url(r'^topic/$', TopicListAPIView.as_view(), name="list"),
    url(r'^topic/(?P<id>.*)/$', TopicGetListAPIView.as_view(), name="topic"),
    url(r'^topics/(?P<key>.*)/$', TopicSourceListAPIView.as_view(), name="topic"),
    url(r'^votes/$', VoteCreateListAPIView.as_view(), name="votes"),
    
]