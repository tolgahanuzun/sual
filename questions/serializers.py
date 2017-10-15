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
        fields = ("user", "body", "date_created")