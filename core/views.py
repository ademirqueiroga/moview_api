from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from movies.models import Movie, Category
from movies.serializers import MovieSerializer, CategorySerializer
from accounts.serializers import UserSerializer
from accounts.models import Profile


class SearchView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):

        result = {}

        if 'username' in request.query_params:
            username = request.query_params['username']
            queryset = User.objects.filter(username__icontains=username)
            result['users'] = UserSerializer(queryset, many=True).data

        if 'title' in request.query_params:
            title = request.query_params['title']
            queryset = Movie.objects.filter(title__icontains=title)
            result['movies'] = MovieSerializer(queryset, many=True).data

        if 'search' in request.query_params:
            query = request.query_params['search']

            #search for users
            queryset = User.objects.filter(username__icontains=query).exclude(pk=request.user.pk)
            usersList = UserSerializer(queryset, many=True).data
            #add following field
            for user in usersList:
                try :
                    request.user.following.get(pk=user['id'])
                    user['followed_by_me'] = True
                except Profile.DoesNotExist:
                    user['followed_by_me'] = False
            result['users'] = usersList

            #search for Movies
            queryset = Movie.objects.filter(title__icontains=query)
            result['movies'] = MovieSerializer(queryset, many=True).data

            #search for categories
            categories = Category.objects.filter(name__icontains=query)
            #result['categories'] = CategorySerializer(categories, many=True).data
            for category in categories:
                queryset = category.movies.all()
                data = MovieSerializer(queryset, many=True).data
                print data
                result['movies'] = result['movies'] + data

        return Response(result, status=status.HTTP_200_OK)
