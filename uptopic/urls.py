from django.conf.urls import url
from uptopic.views import TopicListAPIView, VoteCreateListAPIView, TopicGetListAPIView, TopicSourceListAPIView, UserFollowTopicAPIView, TopicUserListAPIView

urlpatterns = [
    url(r'^topic/$', TopicListAPIView.as_view(), name="list"),
    url(r'^topic/(?P<id>.*)/$', TopicGetListAPIView.as_view(), name="topic"),
    url(r'^topics/(?P<key>.*)/$', TopicSourceListAPIView.as_view(), name="topic"),
    url(r'^follow/topic/$', UserFollowTopicAPIView.as_view(), name="topic_follow"),
    url(r'^follow/topic/(?P<id>.*)/$', TopicUserListAPIView.as_view(), name="user_follow_get"),
    url(r'^votes/$', VoteCreateListAPIView.as_view(), name="votes"),
    
]