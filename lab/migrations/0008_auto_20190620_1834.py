# Generated by Django 2.2.1 on 2019-06-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0007_time_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_slot',
            name='labs',
            field=models.ManyToManyField(related_name='time_slots', to='lab.Lab'),
        ),
    ]
