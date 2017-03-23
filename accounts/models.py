from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile', on_delete=models.CASCADE)
    #picture = models.ImageField(null=True, blank=True, verbose_name='picture')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        ordering = ['user']
