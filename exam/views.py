from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from exam.models import Exam
from exam.serializer import ExamSerializer
# Create your views here.


class ExamViewSet(viewsets.ModelViewSet):
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
