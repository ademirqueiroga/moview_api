from .models import Movie, Category
from .serializers import MovieSerializer, MovieDetailsSerializer, CategorySerializer

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

        serializer = MovieDetailsSerializer(data=data)

        if serializer.is_valid():
            return serializer.save()
        else:
            print serializer.errors
            return


    def get(self, request):
        id = request.path.split('/')[-2]

        movie = Movie.objects.filter(pk=id)
        if movie.count() == 0:
            movie = self.retrieve_of_fetch_details(id)
            return Response(MovieDetailsSerializer(movie).data,
                                status=status.HTTP_200_OK)
        else:
            return Response(MovieDetailsSerializer(movie[0]).data,
                                status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
