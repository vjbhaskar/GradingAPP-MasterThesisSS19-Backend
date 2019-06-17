from django.shortcuts import render
from rest_framework import viewsets
from time_slot.models import Time_Slot
from time_slot.serializer import Time_SlotSerializer
# Create your views here.


class Time_SlotViewSet(viewsets.ModelViewSet):
    queryset = Time_Slot.objects.all()
    serializer_class = Time_SlotSerializer
