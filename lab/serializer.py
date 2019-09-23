from rest_framework import serializers

from exam.models import Exam
from lab.models import Lab, LabIp, Time_Slot
from lab_ip.serializers import LabIpSerializer
from user.serializers import UserSerializer
from user.models import User


class LabSerializer(serializers.ModelSerializer):
    lab_ips = LabIpSerializer(read_only=True, many=True)
    lab_admin = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Lab
        fields = ('id', 'room_building', 'exam', 'date_created', 'date_modified', 'lab_admin', 'lab_ips')
    def create(self, validated_data):
        room_building = validated_data.get('room_building', "")
        # to get request args

        lab_admin_id = self.initial_data['lab_admin']
        exam_id = self.initial_data['exam_id']
        exam = Exam.objects.get(pk=exam_id)
        print('Exam =====',exam)
        print('lab_admin_id==================', lab_admin_id, room_building)
        if lab_admin_id != "":
            lab_admin = User.objects.get(pk=lab_admin_id)
            lab = Lab(room_building=room_building, lab_admin=lab_admin, exam=exam)
            lab.save()
        else:
            lab = Lab(room_building=room_building, exam=exam)
            lab.save()

        # print('lab==================',lab)
        #
        # iparr = self.initial_data['ip_arr']
        #
        # for ip in iparr:
        #     print(ip)
        #     ip_txt = ip
        #     lab_obj = lab
        #     student= None
        #     lab_ip = LabIp(ip=ip_txt, lab=lab_obj, student=student)
        #     lab_ip.save()
        return lab


class Time_SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Time_Slot
        fields = '__all__'
