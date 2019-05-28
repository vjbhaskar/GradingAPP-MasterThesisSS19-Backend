from django.shortcuts import render
from rest_framework.generics import UpdateAPIView
from lab.models import LabIp
from .serializers import LabIpStudentSerializer
# Create your views here.
class LabIpUpdateAPIView(UpdateAPIView):
     queryset= LabIp.objects.all()
     serializer_class=LabIpStudentSerializer
