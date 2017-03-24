from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Profile


class UserSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.first_name + " " + obj.last_name

    def get_followers_count(self, obj):
        return obj.profile.followers.count()

    def get_following_count(self, obj):
        return Profile.objects.filter(followers__id=obj.id).count()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'followers_count', 'following_count')


class RelationshipSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    def get_followers(self, obj):
        queryset = obj.profile.followers.all()
        return UserSerializer(queryset, many=True).data

    def get_following(self, obj):
        queryset = User.objects.filter(profile__followers__id=obj.id)
        return UserSerializer(queryset, many=True).data

    class Meta:
        model = User
        fields = ('followers', 'following')
