from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from questions.models import Questions
from questions.permissions import UserIsOwnerQuestions
from questions.serializers import QuestionsSerializer


class QuestionsMeListAPIView(ListAPIView):
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
