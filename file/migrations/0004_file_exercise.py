# Generated by Django 2.2.2 on 2019-08-22 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_auto_20190820_1753'),
        ('file', '0003_auto_20190630_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='exercise.Exercise'),
        ),
    ]
