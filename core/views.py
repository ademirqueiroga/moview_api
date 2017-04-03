from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from movies.models import Movie, Category
from movies.serializers import MovieSerializer, CategorySerializer
from accounts.serializers import UserSerializer


class SearchView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):

        result = {}

        if 'username' in request.query_params:
            username = request.query_params['username']
            queryset = User.objects.filter(username__iexact=username)
            result['users'] = UserSerializer(queryset, many=True).data

        if 'title' in request.query_params:
            title = request.query_params['title']
            queryset = Movie.objects.filter(title__iexact=title)
            result['movies'] = MovieSerializer(queryset, many=True).data

        if 'search' in request.query_params:
            query = request.query_params['search']

            queryset = User.objects.filter(username__iexact=query)
            result['users'] = UserSerializer(queryset, many=True).data

            queryset = Movie.objects.filter(title__iexact=query)
            result['movies'] = MovieSerializer(queryset, many=True).data

            categories = Category.objects.filter(name__iexact=query)
            result['categories'] = CategorySerializer(categories, many=True).data
            for category in categories:
                queryset = category.movies.all()
                data = MovieSerializer(queryset, many=True).data
                print data
                result['movies'] = result['movies'] + data

        return Response(result, status=status.HTTP_200_OK)
