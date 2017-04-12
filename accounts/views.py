from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer, RelationshipSerializer
from .models import Profile
from movies.serializers import CommentSerializer
from movies.models import Comment

class UserView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):

        if 'username' in request.query_params:
            try:
                username = request.query_params['username']
                user = User.objects.get(username=username)
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                error = {'error': 'Not found'}
                return Response(error, status=status.HTTP_404_NOT_FOUND)

        elif 'id' in request.query_params:
            try:
                user_id = request.query_params['id']
                user = User.objects.get(pk=user_id);
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                error = {'error': 'Not found'}
                return Response(error, status=status.HTTP_404_NOT_FOUND)

        else:
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)


class SignupView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        firt_name = request.data.get('first_name', "")
        last_name = request.data.get('last_name', "")

        users = User.objects.filter(username=username)
        if users.count() > 0:
            return Response({'errors': 'Username already registered.'},
                                    status=status.HTTP_400_BAD_REQUEST)

        users = User.objects.filter(email=email)
        if users.count() > 0:
            return Response({'errors': 'Email already registered.'},
                                    status=status.HTTP_400_BAD_REQUEST)


        user = User.objects.create_user(username=username, email=email,
                                         password=password, first_name=firt_name,
                                         last_name=last_name)

        token, create = Token.objects.get_or_create(user=user)

        data = {
            'user': UserSerializer(user).data,
            'token': token.key
        }
        return Response(data, status=status.HTTP_200_OK)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'user': UserSerializer(user, context={'request': request}).data,
                'token': token.key
            }
            return Response(data, status=status.HTTP_200_OK)

        else:
            return Response({'errors': 'Username or password not correct'},
                                    status=status.HTTP_400_BAD_REQUEST)


class RelationshipView(APIView):

    def get(self, request):
        user = request.user
        data = RelationshipSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)


    def post(self, request):
        user = request.user
        user_id = request.data['user_id']

        already_followed = user.following.filter(pk=user_id).count() > 0
        if already_followed:
            user.following.remove(Profile.objects.get(user_id=user_id))
            data = {'follow': False}
        else:
            user.following.add(Profile.objects.get(user_id=user_id))
            data = {'follow': True}

        return Response(data, status=status.HTTP_200_OK)


class CommentView(APIView):

    def get(self, request):        

        if 'id' in request.query_params:
            user_id = request.query_params['id']
            user = User.objects.get(pk=user_id)
        else:
            user = request.user

        queryset = Comment.objects.filter(user=user).order_by('-created_at')

        data = CommentSerializer(queryset, many=True).data

        return Response(data, status=status.HTTP_200_OK)
