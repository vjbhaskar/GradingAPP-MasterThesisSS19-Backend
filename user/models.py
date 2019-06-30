from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from exam.models import Exam
import uuid


class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (3, 'labadmin'),
      (4, 'admin'),
    )
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, related_name='users', null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(_('email address'), null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

    time_slot = models.ForeignKey('lab.Time_Slot', on_delete=models.SET_NULL, blank=True, null=True)
    ip = models.ForeignKey('lab.LabIp', on_delete=models.SET_NULL, blank=True, null=True)
    login_ip = models.CharField(blank=True, null=True, max_length=255)

    USERNAME_FIELD = 'username'

    # shows username in admin view table instead of Employee Obj
    def __str__(self):
        return "{}".format(self.username)


class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    department = models.CharField(max_length=255,blank=True, null=True)
    photo = models.ImageField(upload_to='uploads',blank=True, null=True)
