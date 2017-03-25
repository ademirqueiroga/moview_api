from rest_framework import serializers
from .models import Movie, Category


class MovieSerializer(serializers.ModelSerializer):

    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        return CategorySerializer(obj.categories.all(), many=True).data

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'release_date', 'poster_path', 'categories')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
         model = Category
         fields = ('id', 'name')
