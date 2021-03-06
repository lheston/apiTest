# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('pubDate', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('coverImg', models.CharField(max_length=200)),
            ],
        ),
    ]
