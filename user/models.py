from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class User(AbstractUser):

    username = models.CharField(unique=True,max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    # shows username in admin view table instead of Employee Obj
    def __str__(self):
        return "{}".format(self.username)
class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (3, 'labadmin'),
      (4, 'admin'),
     )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    fdnumber =models.IntegerField()
    department = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='uploads',null=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
