# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0028_auto_20181128_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trayecto',
            name='estado',
            field=models.IntegerField(default=-1),
        ),
    ]