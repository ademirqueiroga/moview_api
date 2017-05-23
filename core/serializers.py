from rest_framework import serializers

from movies.serializers import MovieSerializer
from accounts.serializers import UserSerializer
from movies.models import Comment


class FeedSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()

    def get_user(self, obj):
        return UserSerializer(obj.user).data

    def get_movie(self, obj):
        return MovieSerializer(obj.movie).data

    class Meta:
        model = Comment
        fields = ('user', 'movie', 'content', 'likes', 'created_at')
