from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework import status

from uptopic.models import Topic, Topic_Questions, Vote_Answer
from uptopic.serializers import TopicSerializer, VoteSerializer, TopicQuestionsSerializer

from questions.models import Answers

class TopicListAPIView(ListCreateAPIView):
    "its own objects"
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"results":'You can not do this without signing in.'}, status=status.HTTP_401_UNAUTHORIZED)


class TopicGetListAPIView(ListAPIView):
    serializer_class = TopicQuestionsSerializer
    permission_classes = ()

    def get_queryset(self):
        return Topic_Questions.objects.filter(topic=Topic.objects.filter(name__icontains=self.kwargs['key']))

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        if not queryset:
            return Response({"results":"Topic or content not found!"}, status=status.HTTP_204_NO_CONTENT)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
