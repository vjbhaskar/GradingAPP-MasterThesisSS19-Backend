from django.shortcuts import render
from rest_framework import viewsets
from exam.models import Exam
from exam.serializer import ExamSerializer
# Create your views here.


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
