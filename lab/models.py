from django.db import models
from django.db.models.signals import post_save

from exam.models import Exam


# Create your models here.
class Lab(models.Model):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    lab_admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lab', blank=True, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, blank=True, null=True)
    room_building = models.CharField(unique=True, max_length=255)
    file_obj = models.FileField(upload_to='uploads', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{x} - {y}'.format(x=self.pk, y=self.room_building)


class LabIp(models.Model):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='lab_ips')
    ip = models.CharField(max_length=255, blank=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['lab', 'ip']
        db_table = 'lab_ips'
        ordering = ['-date_created']

    def __str__(self):
        return '{} - ID={}'.format(self.ip, self.lab.pk)


class Time_Slot(models.Model):
    labs = models.ManyToManyField(Lab, through='TimeSlotLabMembership')
    name = models.CharField(unique=True, max_length=255)
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "time_slots"


class TimeSlotLabMembership(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(Time_Slot, on_delete=models.CASCADE)

    class Meta:
        db_table = 'timeslot_lab_memberships'

    def __str__(self):
        return '{} - {}'.format(self.lab.room_building, self.time_slot.name)


def allocate_timeslots_to_labs(**kwargs):
    labs = Lab.objects.all()
    instance = kwargs['instance']

    for lab in labs:
        TimeSlotLabMembership(lab=lab, time_slot=instance).save()


post_save.connect(allocate_timeslots_to_labs, sender=Time_Slot)
