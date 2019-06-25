from django.db import models
# from exam.models import Exam


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255)
    # exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
