from .models import *
from .serializers import *

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

import json, requests, urllib

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny,)

class MovieDetailsView(APIView):
    permission_classes = (AllowAny,)

    def retrieve_of_fetch_details(self, id):
        urlMovieDetails = "https://api.themoviedb.org/3/movie/" + str(id) + "?"
        api_key = "15e1fa139021ce8ffbda7a3ca062f2fc"
        url = urlMovieDetails + str(urllib.urlencode({'api_key': api_key}))

        response = requests.get(url)
        data = response.json()

        print data

        if data['status_code'] != 34:
            serializer = MovieDetailsSerializer(data=data)

            if serializer.is_valid():
                return serializer.save()
            else:
                print serializer.errors
                return None


    def get(self, request):
        id = request.path.split('/')[-2]

        try:
            movie = Movie.objects.filter(pk=id)
            return Response(MovieDetailsSerializer(movie[0]).data,
                                status=status.HTTP_200_OK)
        except:
            movie = self.retrieve_of_fetch_details(id)
            if movie is None:
                return Response({'errors': 'content not found'},
                                    status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(MovieDetailsSerializer(movie).data,
                                    status=status.HTTP_200_OK)


class CommentView(APIView):

    def get(self, request):
        user = request.user

        #query for comments of a movie
        if 'movie' in request.query_params:
            movie_id = request.query_params['movie']
            queryset = Comment.objects.filter(movie_id=movie_id)

        #query for comments of a user
        elif 'user' in request.query_params:
            user_id = request.query_params['user']
            queryset = Comment.objects.filter(user_id=user_id)

        #query for comments of request.user
        else:
            queryset = Comment.objects.filter(user=user)

        data = CommentSerializer(queryset, many=True).data

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user;

        try:
            movie = Movie.objects.get(pk=request.data['movie'])
        except Movie.DoesNotExist:
            return Response({'error': 'movie not found'},status=status.HTTP_400_BAD_REQUEST)

        content = request.data['content']
        comment = Comment(user=user, movie=movie, content=content, likes=0)
        comment.save()

        return Response(status=status.HTTP_201_CREATED)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
