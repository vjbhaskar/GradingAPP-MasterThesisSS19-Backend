from django.db import models
from user.models import User

# Create your models here.
class File(models.Model):
    name= models.CharField(unique=True,max_length=255)
    is_submitted= models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    file_obj = models.FileField(upload_to='uploads',null=True)
    creator_id = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='files')
    file_binary = models.BinaryField(null=True)
