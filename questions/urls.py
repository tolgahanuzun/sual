from django.conf.urls import url
from questions.views import QuestionsMeListAPIView, QuestionsListCreateAPIView, QuestionsDetailAPIView

urlpatterns = [
    url(r'^$', QuestionsListCreateAPIView.as_view(), name="list"),
    url(r'^me/$', QuestionsMeListAPIView.as_view(), name="me_list"),
    url(r'^(?P<pk>[0-9]+)/$', QuestionsDetailAPIView.as_view(), name="detail"),
]