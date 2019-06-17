from django.db import models

# Create your models here.
class Time_Slot(models.Model):
    name= models.CharField(unique=True,max_length=255)
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
