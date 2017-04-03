# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.Movie'),
            preserve_default=False,
        ),
    ]
