from django.conf.urls import url
from uptopic.views import TopicListAPIView, VoteCreateListAPIView, TopicGetListAPIView

urlpatterns = [
    url(r'^topic/$', TopicListAPIView.as_view(), name="list"),
    url(r'^topics/(?P<key>.*)/$', TopicGetListAPIView.as_view(), name="topic"),
    url(r'^votes/$', VoteCreateListAPIView.as_view(), name="votes"),
    
]