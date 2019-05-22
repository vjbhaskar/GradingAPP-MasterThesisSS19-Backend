from rest_framework import serializers
from lab.models import Lab, LabIp
from user.serializers import UserSerializer
from user.models import User
from .ip_serializer import LabIpSerializer

class LabIpSerializer(serializers.ModelSerializer):
    lab = LabSerializer(read_only=True, many=False)
    student = UserSerializer(read_only=True)

    class Meta:
        model = LabIp
        fields = ('id', 'ip', 'lab', 'date_created', 'date_modified',
        'student')

    def create(self, validated_data):
        ip = validated_data.get('ip',"")
        # ip = self.initial_data['lab_id']
        # to get request args
        lab_id = self.initial_data['lab_id']
        student_id = self.initial_data['student_id']
        print('student_id ============',self.initial_data['student_id'])
        print('lab id ============',self.initial_data['lab_id'])
        student = User.objects.get(pk=student_id)
        lab = Lab.objects.get(pk=lab_id)
        lab_ip= LabIp(ip=ip,lab=lab,student=student)
        lab_ip.save()
        return lab


class LabSerializer(serializers.ModelSerializer):
    lab_ips = LabIpSerializer(read_only=True, many=True)
    lab_admin = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Lab
        fields = ('id', 'room_building', 'date_created', 'date_modified',
        'lab_admin', 'lab_ips')

    def create(self, validated_data):
        room_building = validated_data.get('room_building',"")
        # to get request args
        lab_admin_id = self.initial_data['lab_admin']
        print('lab_admin ============',self.initial_data['lab_admin'])
        lab_admin = User.objects.get(pk=lab_admin_id)
        lab= Lab(room_building=room_building,lab_admin=lab_admin)
        lab.save()
        return lab
