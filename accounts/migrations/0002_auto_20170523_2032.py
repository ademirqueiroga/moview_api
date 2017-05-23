# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20170522_2222'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='profile',
            name='watchlist',
            field=models.ManyToManyField(related_name='watchlist', to='movies.Movie'),
        ),
    ]