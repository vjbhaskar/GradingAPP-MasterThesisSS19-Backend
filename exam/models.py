from django.db import models


from subject.models import Subject
#from exercise.models import Exercise
# from django.contrib.auth import get_user_model


# User = get_user_model()


# Create your models here.
class Exam(models.Model):
    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='exam', blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')
    name = models.CharField(unique=True, max_length=255)
    #exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='exercise', blank=True,null=True)
    # TBD More fields
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'exam: {}  subject: {}'.format(self.name, self.subject.name)




