# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-17 12:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='subject.Subject'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='time_slot1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='time_slot1', to='time_slot.Time_Slot'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='time_slot2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='time_slot2', to='time_slot.Time_Slot'),
        ),
    ]
