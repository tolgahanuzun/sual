from django.conf.urls import url
from questions.views import QuestionsMeListAPIView, QuestionsListCreateAPIView, QuestionsDetailAPIView, \
AnswersListCreateAPIView, AnswersDetailAPIView

urlpatterns = [
    url(r'^question/$', QuestionsListCreateAPIView.as_view(), name="list"),
    url(r'^question/me/$', QuestionsMeListAPIView.as_view(), name="me_list"),
    url(r'^question/(?P<pk>[0-9]+)/$', QuestionsDetailAPIView.as_view(), name="user-detail"),

    url(r'^answer/$', AnswersListCreateAPIView.as_view(), name="list"),
    url(r'^answer/(?P<pk>[0-9]+)/$', AnswersDetailAPIView.as_view(), name="answer-detail"),
]