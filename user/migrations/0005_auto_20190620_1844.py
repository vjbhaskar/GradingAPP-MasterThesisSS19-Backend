# Generated by Django 2.2.1 on 2019-06-20 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_auto_20190620_1834'),
        ('user', '0004_auto_20190620_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='timeslot',
        ),
        migrations.AddField(
            model_name='user',
            name='ip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lab.LabIp'),
        ),
        migrations.AddField(
            model_name='user',
            name='time_slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lab.Time_Slot'),
        ),
    ]