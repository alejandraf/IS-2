# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_auto_20170426_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='pathToTemplate',
            field=models.CharField(max_length=50),
        ),
    ]
