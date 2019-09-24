from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer
# Create your views here.


class ExerciseViewSet(viewsets.ModelViewSet):

    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
