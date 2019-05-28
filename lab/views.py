from django.shortcuts import render
from rest_framework import viewsets
from lab.models import Lab,LabIp
from lab.serializer import LabSerializer
from lab_ip.serializers import LabIpStudentSerializer
# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from lab_ip.serializers import LabIpSerializer


class LabViewSet(viewsets.ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

class LabIpViewSet(viewsets.ModelViewSet):
    queryset = LabIp.objects.all()
    serializer_class = LabIpSerializer
