from rest_framework import serializers

from django.contrib.auth.models import User

#from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    #profile = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile')
