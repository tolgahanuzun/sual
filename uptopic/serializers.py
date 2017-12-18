from django.contrib.auth.models import User
from rest_framework import serializers

from uptopic.models import Topic_Questions, Topic, Vote_Answer
from profiles.serializers import UserSerializer
from questions.serializers import AnswersSerializer, ClearQuestionsSerializer
from questions.models import Questions


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ("id", "name", "tittle", "about", "image")


class TopicQuestionsSerializer(serializers.ModelSerializer):
    questions = ClearQuestionsSerializer(read_only=True)

    class Meta:
        model = Topic_Questions
        fields = ("topic","questions")

class VoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    answer = AnswersSerializer(read_only=True)

    class Meta:
        model = Vote_Answer
        fields = ("id", "user", "answer", "type")
