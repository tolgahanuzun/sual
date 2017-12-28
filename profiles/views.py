from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import UserProfile
from questions.models import Questions
from profiles.serializers import UserRegistrationSerializer, UserLoginSerializer, TokenSerializer, UserProfileSerializer, QuestionsSerializer


class UserRegistrationAPIView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance.user
        token, created = Token.objects.get_or_create(user=user)
        data = serializer.data
        data["token"] = token.key

        headers = self.get_success_headers(serializer.data)


        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginAPIView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                data=TokenSerializer(token).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserLogoutAPIView(APIView):

    def post(self, request, *args, **kwargs):
        Token.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_200_OK)

class UserGetAPI(APIView):
    permission_classes = ()

    def get(self, request, username):
        serializer_users = UserProfileSerializer(UserProfile.objects.filter(user__username__iregex=username), many=True)
        serializer_questions = QuestionsSerializer(Questions.objects.filter(user__username__iregex=username), many=True)

        if serializer_users.data or False:
            if serializer_questions.data or None:
                serializer = {'user_details':serializer_users.data[0], 'questions_details':[serializer_questions.data[0]]}
            else:
                serializer = {'user_details':serializer_users.data[0], 'questions_details':'Null'}
                
            return Response(
                data=serializer
                #status=status.HTTP_200_OK,
                )
        else:
            return Response(
                data = {'results':'No members found.'},
                status=status.HTTP_400_BAD_REQUEST,
            )


class TokenUsers(APIView):

    def get(self, request, format=None):
        return Response({'id':request.user.id})
