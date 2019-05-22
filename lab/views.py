from django.shortcuts import render
from rest_framework import viewsets
from lab.models import Lab,LabIp
from lab.serializer import LabSerializer
from lab.ip_serializer import LabIpSerializer
# Create your views here.


class LabViewSet(viewsets.ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

class LabIpViewSet(viewsets.ModelViewSet):
    queryset = LabIp.objects.all()
    serializer_class = LabIpSerializer
