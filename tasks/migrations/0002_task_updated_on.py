# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]