from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):
    #category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    synopsis = models.TextField()
    main_cast = models.TextField()
    duration = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    cover_image = models.ImageField(verbose_name='image')
    #rating = models.FloatField()
