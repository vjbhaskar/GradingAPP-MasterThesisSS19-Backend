# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-24 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190622_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_ip',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
