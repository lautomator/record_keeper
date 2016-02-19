# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader_title', models.CharField(max_length=80)),
                ('reader_entry', models.TextField()),
                ('reader_date', models.DateTimeField(auto_now=True)),
                ('reader_author', models.CharField(default='admin', max_length=80)),
            ],
        ),
    ]
