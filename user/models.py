from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import uuid


class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (3, 'labadmin'),
      (4, 'admin'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True,max_length=255)
    email = models.EmailField(_('email address'),null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

    USERNAME_FIELD = 'username'

    # shows username in admin view table instead of Employee Obj
    def __str__(self):
        return "{}".format(self.username)


class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    department = models.CharField(max_length=255,blank=True, null=True)
    photo = models.ImageField(upload_to='uploads',blank=True, null=True)
