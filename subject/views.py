from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from subject.models import Subject
from subject.serializer import SubjectSerializer
# Create your views here.


class SubjectViewSet(viewsets.ModelViewSet):
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
