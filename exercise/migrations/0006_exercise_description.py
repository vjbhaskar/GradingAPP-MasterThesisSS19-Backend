# Generated by Django 2.2.2 on 2019-08-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_auto_20190820_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
