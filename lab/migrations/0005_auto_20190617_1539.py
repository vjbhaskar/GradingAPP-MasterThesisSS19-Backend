# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-17 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_lab_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='exam.Exam'),
        ),
    ]