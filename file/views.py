from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from file.models import File
from file.serializers import FileSerializer
# Also add these imports
# from user.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class FileListCreateAPIView(ListCreateAPIView):
    queryset=File.objects.all()
    serializer_class=FileSerializer

class FileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=File.objects.all()
    serializer_class=FileSerializer
    lookup_field='id'
