from rest_framework import serializers
from .models import Movie, Category, Comment


class MovieSerializer(serializers.ModelSerializer):

    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        return CategorySerializer(obj.categories.all(), many=True).data

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'release_date', 'poster_path', 'categories')

class MovieDetailsSerializer(serializers.ModelSerializer):

    categories = serializers.SerializerMethodField()
    following_comments = serializers.SerializerMethodField();

    def get_categories(self, obj):
        return CategorySerializer(obj.categories.all(), many=True).data

    def get_following_comments(self, obj):
        user = self.context['request'].user
        return obj.comments.filter(user__profile__in=user.following.all()).count()

    class Meta:
        model = Movie
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
         model = Category
         fields = ('id', 'name')


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()
    movie_title = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.id

    def get_username(self, obj):
        return obj.user.username

    def get_movie(self, obj):
        return obj.movie.id

    def get_movie_title(self, obj):
        return obj.movie.title

    class Meta:
        model = Comment
        fields = ('user', 'username', 'movie', 'movie_title', 'content', 'likes', 'created_at')
