# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20161117_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='usuar',
            field=models.CharField(max_length=120),
        ),
    ]