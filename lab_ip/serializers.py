from rest_framework import serializers
from lab.models import Lab, LabIp
from user.serializers import UserSerializer
from user.models import User


class LabIpSerializer(serializers.ModelSerializer):
    # lab = LabSerializer(read_only=True, many=False)
    student1 = UserSerializer(read_only=True)
    student2 = UserSerializer(read_only=True)

    class Meta:
        model = LabIp
        fields = ('id', 'ip', 'lab', 'date_created', 'date_modified', 'student1','student2')
        read_only_fields = ('lab',)
        depth = 2

    def create(self, validated_data):
        ip = self.initial_data.get('ip', '')
        print(self.initial_data)
        # ip = validated_data.get('ip', "")
        # ip = self.initial_data['lab_id']
        # to get request args
        lab_id = self.initial_data['lab_id']
        student_id = self.initial_data['student_id']
        print('student_id ============', self.initial_data['student_id'])
        print('lab id ============', self.initial_data['lab_id'])
        student = User.objects.get(pk=student_id)
        print(student)
        lab = Lab.objects.get(pk=lab_id)
        lab_ip = LabIp(ip=ip, lab=lab, student=student)
        lab_ip.save()
        return lab_ip


class LabIpStudentSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)

    class Meta:
        model = LabIp
        fields = ('id', 'ip', 'lab', 'date_created', 'date_modified', 'student')
        read_only_fields = ('lab',)

    # def update(self, validated_data):
    #     print('debba=================',self.initial_data)
    #     lab_id = self.initial_data['lab_id']
    #     studentarr = self.initial_data['student_arr']
    #     print('studentObj=================',studentarr,lab_id)
    #     for student in studentarr:
    #         print(student)
    #         studentObj = User.objects.get(pk=student_id)
    #         print('studentObj=================',studentObj)
    #     # student = User.objects.get(pk=student_id)
    #     # print(student)
    #     # lab = Lab.objects.get(pk=lab_id)
    #     # lab_ip = LabIp(ip=ip, lab=lab, student=student)
    #     # lab_ip.save()
    #     return lab_ip
