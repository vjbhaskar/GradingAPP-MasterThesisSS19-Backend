from django.shortcuts import render
from rest_framework import viewsets
from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer
# Create your views here.


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
