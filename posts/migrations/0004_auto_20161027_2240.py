# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 22:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20161027_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='alb',
            new_name='nombrealbum',
        ),
    ]
