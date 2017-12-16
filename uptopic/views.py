from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework import status

from uptopic.models import Topic, Topic_Questions, Vote_Answer
from uptopic.serializers import TopicSerializer, VoteSerializer

from questions.models import Answers

class TopicListAPIView(ListAPIView):
    "its own objects"
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = ()

class VoteCreateListAPIView(ListCreateAPIView):
    "Vote create and Vote now data result"
    serializer_class = VoteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        answer = Answers.objects.get(id=self.request.data['answer'])
        last_vote = Vote_Answer.objects.filter(answer=answer, user=self.request.user)
        last_vote.delete()

        serializer.save(user=self.request.user, answer=answer, type=self.request.data['type'])
        headers = self.get_success_headers(serializer.data)
        

        result = request.data
        upvote = len(Vote_Answer.objects.filter(type="True", answer=answer))
        downvote = len(Vote_Answer.objects.filter(type="False", answer=answer))
        result['vote'] = upvote - downvote

        return Response(result, status=status.HTTP_201_CREATED, headers=headers)

