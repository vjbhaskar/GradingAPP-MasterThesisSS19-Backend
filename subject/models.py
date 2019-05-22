from django.db import models

# Create your models here.
class Subject(models.Model):
    name= models.CharField(unique=True,max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
