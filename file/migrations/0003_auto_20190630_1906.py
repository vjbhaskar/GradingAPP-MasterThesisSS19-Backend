# Generated by Django 2.2.2 on 2019-06-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_file_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
