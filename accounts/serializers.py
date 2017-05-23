from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Profile
from movies.models import Comment
from movies.serializers import MovieSerializer

class UserSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.first_name + " " + obj.last_name

    def get_followers_count(self, obj):
        return obj.profile.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'followers_count', 'following_count')


class ProfileSerializer(serializers.ModelSerializer):

    favorites = serializers.SerializerMethodField()
    watchlist = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    def get_favorites(self, obj):
        queryset = obj.favorites.all()
        return MovieSerializer(queryset, many=True).data

    def get_watchlist(self, obj):
        queryset = obj.watchlist.all()
        return MovieSerializer(queryset, many=True).data

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.user.following.count()

    class Meta:
        model = Profile
        fields = ('picture', 'favorites', 'watchlist', 'followers_count', 'following_count')


class RelationshipSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    def get_followers(self, obj):
        queryset = obj.profile.followers.all()
        return UserSerializer(queryset, many=True).data

    def get_following(self, obj):
        queryset = User.objects.filter(following__id=obj.id)
        return UserSerializer(queryset, many=True).data

    class Meta:
        model = User
        fields = ('followers', 'following')
