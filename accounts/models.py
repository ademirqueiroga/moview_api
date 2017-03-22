from __future__ import unicode_literals

from django.db import models

class Profile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile', on_delete=models.CASCADE)
    #picture = models.ImageField(null=True, blank=True, verbose_name='picture')


    def __str__(self):
        return self.user.email


    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        ordering = ['user']
