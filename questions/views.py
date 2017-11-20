from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from questions.models import Questions, Answers
from questions.permissions import UserIsOwnerQuestions
from questions.serializers import QuestionsSerializer, AnswersSerializer


class QuestionsMeListAPIView(ListAPIView):
    "its own objects"
    serializer_class = QuestionsSerializer

    def get_queryset(self):
        return Questions.objects.filter(user=self.request.user)


class QuestionsListCreateAPIView(ListCreateAPIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuestionsDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    permission_classes = (IsAuthenticated, UserIsOwnerQuestions)


class AnswersMeListAPIView(ListAPIView):
    "its own objects"
    serializer_class = AnswersSerializer

    def get_queryset(self):
        return Answers.objects.filter(user=self.request.user)


class AnswersListCreateAPIView(ListCreateAPIView):
    serializer_class = AnswersSerializer
    queryset = Answers.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AnswersDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnswersSerializer
    queryset = Answers.objects.all()
    permission_classes = (IsAuthenticated)
