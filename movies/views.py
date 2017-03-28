from .models import Movie, Category
from .serializers import MovieSerializer, MovieDetailsSerializer, CategorySerializer

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailsView(APIView):    

    def get(self, request):
        id = request.path.split('/')[-2]

        movie = Movie.objects.get(pk=id)

        return Response(MovieDetailsSerializer(movie).data,
                            status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
