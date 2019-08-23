from django.db import models

# Create your models here.
from exam.models import Exam
from subject.models import Subject


class Exercise(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exercise', blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
   # file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='files')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
