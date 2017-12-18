from django.contrib.auth.models import User
from rest_framework import serializers
from questions.models import Questions, Answers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class QuestionsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Questions
        fields = ("user", "body", "date_created","id")


class ClearQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ("user", "body", "date_created","id")


class AnswersGETSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ("body", "date_created", "id")

class QuestionsGETSerializer(serializers.ModelSerializer):
    answers_set = AnswersGETSerializer(read_only=True, many=True)

    class Meta:
        model = Questions
        fields = ("answers_set", "body", "date_created", "id")


class AnswersSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    question = QuestionsSerializer(read_only=True)

    class Meta:
        model = Answers
        fields = ("owner", "question", "body", "date_created", "id")
