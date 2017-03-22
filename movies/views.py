from .models import Movie
from .serializers import MovieSerializer

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
# Create your views here.

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny,)
