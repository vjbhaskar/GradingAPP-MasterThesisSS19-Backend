# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-17 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_exam_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='user',
        ),
    ]