from django.db import models
from django.contrib.auth import get_user_model
from exam.models import Exam


User = get_user_model()


# Create your models here.
class Lab(models.Model):
    lab_admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lab')
    exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, blank=True, null=True)
    room_building= models.CharField(unique=True,max_length=255)
    file_obj = models.FileField(upload_to='uploads',blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{x} - {y}'.format(x=self.pk, y=self.lab_admin.username)


class LabIp(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='lab_ips')
    student1 = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='std1_lab_ip',
        blank=True,
        null=True
    )
    student2 = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='std2_lab_ip',
        blank=True,
        null=True
    )
    ip = models.CharField(max_length=255, blank=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['lab', 'ip']
        db_table = 'lab_ips'
        ordering = ['-date_created']

    def __str__(self):
        return '{} - ID={}'.format(self.ip, self.lab.pk)
