from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Lab(models.Model):
    room_building= models.CharField(unique=True,max_length=255)
    lab_admin = models.ForeignKey(User,on_delete=models.CASCADE, related_name='lab')
    file_obj = models.FileField(upload_to='uploads',blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{x} - {y}'.format(x=self.pk, y=self.lab_admin.username)


class LabIp(models.Model):
    ip = models.CharField(max_length=255, blank=True, unique=True)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='lab_ips')
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='lab_ip', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['student', 'lab', 'ip']
        db_table = 'lab_ips'
        ordering = ['-date_created']

    def __str__(self):
        return '{} - {}'.format(self.ip, self.lab.pk)
