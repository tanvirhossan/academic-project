# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alllist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=300)),
                ('pimage', models.FileField(blank=True, null=True, upload_to='')),
                ('placediscription', models.TextField()),
                ('placeway', models.TextField()),
                ('imagefigname', models.CharField(max_length=100)),
                ('shortdiscription', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['uname'],
            },
        ),
    ]