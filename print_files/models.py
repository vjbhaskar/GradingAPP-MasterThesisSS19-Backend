from django.db import models
from user.models import User
from subject.models import Subject
# Create your models here.


class Print_File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='print_files')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='print_files')
    name = models.CharField(max_length=255)
    is_submitted = models.BooleanField(default=False)
    file_obj = models.FileField(upload_to='uploads', null=True)
    is_snippet = models.BooleanField(default=False)
    file_binary = models.BinaryField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

