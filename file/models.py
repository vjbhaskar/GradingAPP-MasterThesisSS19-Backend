from django.db import models
from user.models import User
from subject.models import Subject
from exercise.models import Exercise
# Create your models here.


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='files')
    name = models.CharField(max_length=255)
    is_submitted = models.BooleanField(default=False)
    file_obj = models.FileField(upload_to='uploads', null=True)
    # Remove in future creator_id is redundant
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, related_name='files')
    creator_id = models.CharField(max_length=255)
    file_binary = models.BinaryField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

