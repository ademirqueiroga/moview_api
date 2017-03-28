from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['id']

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    categories = models.ManyToManyField(Category, related_name='movies')
    release_date = models.CharField(max_length=15)
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(default='', blank=True, max_length=100)
    budget = models.IntegerField(default=0, blank=True)
    revenue = models.IntegerField(default=0, blank=True)
    runtime = models.IntegerField(default=0, blank=True)
    rating = models.FloatField(default=0.0, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'
        ordering = ['id']
