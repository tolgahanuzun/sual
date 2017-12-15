from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _


from rest_framework import serializers
from rest_framework.authtoken.models import Token

from profiles.models import UserProfile
from questions.models import Questions

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    company = serializers.CharField(write_only=False)
    tittle = serializers.CharField(write_only=False)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "tittle", "company")

    def create(self, validated_data):
        if validated_data.get('password'):
            validated_data['password'] = make_password(
                validated_data['password']
            )
        validated_data.pop('tittle'); validated_data.pop('company')
        user = get_user_model().objects.create(**validated_data)
        profile_user = UserProfile.objects.create(user=user, tittle=self.data['tittle'], company=self.data['company'])
        
        return profile_user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {
        'inactive_account': _('User account is disabled.'),
        'invalid_credentials': _('User not found!')
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(username=attrs.get("username"), password=attrs.get('password'))
        print(self.user)
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("auth_token",)



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")

class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ("id", "body", "date_created")


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ("user", "company", "tittle")
        related_object = 'user'

