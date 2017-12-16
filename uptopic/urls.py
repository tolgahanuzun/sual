from django.conf.urls import url
from uptopic.views import TopicListAPIView, VoteCreateListAPIView

urlpatterns = [
    url(r'^topic/$', TopicListAPIView.as_view(), name="list"),
    url(r'^votes/$', VoteCreateListAPIView.as_view(), name="votes"),
    
]