# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-29 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0011_auto_20180125_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='previus_id',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]