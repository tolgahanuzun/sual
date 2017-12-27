from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework import status

from uptopic.models import Topic, Topic_Questions, Vote_Answer
from uptopic.serializers import TopicSerializer, VoteSerializer, TopicQuestionsSerializer, TopicSearceQuestionsSerializer
from questions.serializers import ClearQuestionsSerializer
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
    pagination_class = None

    def get_queryset(self):
        return Topic.objects.filter(id=self.kwargs['id'])
    
    def sub_query_clear(self, data):
        newdata = list()
        for i in range(len(data)):
            temps = data[i].questions
            newdata.append(temps)
            
        return newdata

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            return Response({"results":"Topic or content not found!"}, status=status.HTTP_204_NO_CONTENT)

        serializer_topic = self.get_serializer(queryset, many=True)
        sub_query = Topic_Questions.objects.filter(topic=self.get_queryset()[0])
        query_clear = self.sub_query_clear(sub_query)
        serializer_questions = ClearQuestionsSerializer(query_clear, many=True)

        if serializer_topic.data or False:
            if serializer_questions.data or None:
                serializer = {'topic_details':serializer_topic.data[0], 'questions_details':serializer_questions.data}
            else:
                serializer = {'topic_details':serializer_topic.data[0], 'questions_details':'Null'}

            return Response(data=serializer)


class TopicSourceListAPIView(ListAPIView):
    serializer_class = TopicSerializer
    permission_classes = ()
    pagination_class = None

    def get_queryset(self):
        return Topic.objects.filter(name__icontains=self.kwargs['key'])

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset:
            return Response({"results":"Topic or content not found!"}, status=status.HTTP_204_NO_CONTENT)

        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)

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
