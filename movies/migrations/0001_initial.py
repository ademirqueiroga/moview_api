# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('synopsis', models.TextField()),
                ('main_cast', models.TextField()),
                ('duration', models.PositiveSmallIntegerField()),
                ('year', models.PositiveSmallIntegerField()),
                ('cover_image', models.ImageField(upload_to=b'', verbose_name='image')),
            ],
        ),
    ]
