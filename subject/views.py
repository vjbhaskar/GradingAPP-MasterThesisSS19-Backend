from django.shortcuts import render
from rest_framework import viewsets
from subject.models import Subject
from subject.serializer import SubjectSerializer
# Create your views here.


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
