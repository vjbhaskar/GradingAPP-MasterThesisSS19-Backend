from rest_framework import serializers


from lab.models import Lab, LabIp
from lab_ip.serializers import LabIpSerializer
from user.serializers import UserSerializer
from user.models import User
import csv
from io import StringIO
import io

class LabSerializer(serializers.ModelSerializer):
    lab_ips = LabIpSerializer(read_only=True, many=True)
    lab_admin = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Lab
        fields = ('id', 'room_building', 'date_created', 'date_modified', 'lab_admin', 'lab_ips')

    def create(self, validated_data):
        # file_obj =  validated_data.get('file_obj',"")
        # print('file_obj===============================',validated_data.get('file_obj',""))
        # csv_file = file_obj
        # decoded_file = csv_file.read().decode('utf-8')
        # io_string = io.StringIO(decoded_file)
        # for line in csv.reader(io_string, delimiter=',', quotechar='|'):
        #     print(line)

        room_building = validated_data.get('room_building',"")
        # to get request args

        lab_admin_id = self.initial_data['lab_admin']
        print('lab_admin_id==================',lab_admin_id,room_building)
        lab_admin = User.objects.get(pk=lab_admin_id)
        lab= Lab(room_building=room_building,lab_admin=lab_admin)
        lab.save()
        print('lab==================',lab)
        iparr = self.initial_data['ip_arr']
        for ip in iparr:
            print(ip)
            ip_txt = ip
            lab_obj = lab
            student= None
            lab_ip = LabIp(ip=ip_txt, lab=lab_obj, student=student)
            lab_ip.save()
        return lab
