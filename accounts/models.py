from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    picture = models.ImageField(null=True, blank=True, verbose_name='picture')
    followers = models.ManyToManyField(User, related_name='following')

    #TODO
    #add two integer fields for followers_count and following_count
    #to remove extra query from UserSerializer

    def create_profile(sender, **kwargs):
        user = kwargs['instance']
        if kwargs['created']:
            profile = Profile(user=user)
            profile.save()

    post_save.connect(create_profile, sender=User)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        ordering = ['user']
