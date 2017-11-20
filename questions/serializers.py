from django.contrib.auth.models import User
from rest_framework import serializers
from questions.models import Questions


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class QuestionsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Questions
        fields = ("user", "body", "date_created","id")


class AnswersSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    question = QuestionsSerializer(read_only=True)

    class Meta:
        model = Questions
        fields = ("owner", "question", "body", "date_created","id")
