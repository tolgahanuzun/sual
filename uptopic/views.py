from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, GenericAPIView
from rest_framework.mixins import  CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework import status

from uptopic.models import Topic, Topic_Questions, Vote_Answer, Topic_Users
from uptopic.serializers import TopicSerializer, VoteSerializer, TopicQuestionsSerializer, TopicSearceQuestionsSerializer, FollowSerializer, TopicUserListSerializer
from questions.serializers import ClearQuestionsSerializer
from questions.models import Answers

from profiles.models import UserProfile

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


class UserFollowTopicAPIView(CreateModelMixin, DestroyModelMixin, GenericAPIView):
    permission_classes = ()
    serializer_class = FollowSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            topic = Topic.objects.get(id=self.request.data['topic_id'])
            user = UserProfile.objects.get(user=self.request.user)
        except ValueError:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        follow = Topic_Users.objects.filter(topic=topic, user=user)
        if follow:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer.save(user=user, topic=topic)

        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        try:
            topic = Topic.objects.get(id=self.request.data['topic_id'])
            user = UserProfile.objects.get(user=self.request.user)
        except:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        follow = Topic_Users.objects.filter(topic=topic, user=user)
        if not follow:
            return Response(status=status.HTTP_404_NOT_FOUND)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TopicUserListAPIView(ListAPIView):
    serializer_class = TopicUserListSerializer
    permission_classes = ()

    def get_queryset(self):
        return Topic.objects.filter(id=self.kwargs['id'])

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        
        allrecord = Topic_Users.objects.filter(topic=queryset[0]) 
        if not allrecord:
            return Response({"results":"Topic or content not found!"}, status=status.HTTP_204_NO_CONTENT)
        
        getusers = list()
        for record in allrecord:
            getusers.append(record.user)
        
        serializer = self.get_serializer(getusers, many=True)
        return Response(data=serializer.data)