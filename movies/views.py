from .models import Movie, Category
from .serializers import MovieSerializer, CategorySerializer

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
# Create your views here.

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny,)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
