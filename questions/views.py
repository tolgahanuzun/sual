from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from questions.models import Questions, Answers
from questions.permissions import UserIsOwnerQuestions
from questions.serializers import QuestionsSerializer, AnswersSerializer, QuestionsGETSerializer

from uptopic.models import Vote_Answer

class QuestionsMeListAPIView(ListAPIView):
    "its own objects"
    serializer_class = QuestionsSerializer

    def get_queryset(self):
        return Questions.objects.filter(user=self.request.user)


class QuestionsListCreateAPIView(ListCreateAPIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    permission_classes = ()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuestionsDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionsGETSerializer
    queryset = Questions.objects.all()
    permission_classes = ()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        vote = serializer.data

        for v in range(len(vote['answers_set'])):
            upvote = len(Vote_Answer.objects.filter(type="True",
                answer=instance.answers_set.get(id=vote['answers_set'][v]['id'])))
            downvote = len(Vote_Answer.objects.filter(type="False",
                answer=instance.answers_set.get(id=vote['answers_set'][v]['id'])))
            vote['answers_set'][v]['vote']= upvote - downvote


        return Response(vote)

class AnswersListCreateAPIView(ListCreateAPIView):
    serializer_class = AnswersSerializer

    def get_queryset(self):
        return Answers.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        question = Questions.objects.get(id=self.request.data['question'])
        serializer.save(owner=self.request.user, question=question)


class AnswersDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnswersSerializer
    queryset = Answers.objects.all()
    permission_classes = ()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        vote_serializer = serializer.data

        upvote = len(Vote_Answer.objects.filter(type="True", answer=instance))
        downvote = len(Vote_Answer.objects.filter(type="False", answer=instance))
        vote_serializer['vote'] = upvote - downvote

        return Response(vote_serializer)