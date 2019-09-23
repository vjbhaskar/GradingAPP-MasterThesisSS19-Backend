import json
import random
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import UpdateAPIView
from exam.models import Exam
from lab.models import LabIp,Lab,Time_Slot
from .serializers import LabIpStudentSerializer
import io
import csv

User = get_user_model()


# Create your views here.
class LabIpUpdateAPIView(UpdateAPIView):
    queryset = LabIp.objects.all()
    serializer_class = LabIpStudentSerializer

# Function based view
@csrf_exempt
@api_view(['POST', ])
# @permission_classes([permissions.IsAdminUser, ])
def assign_ips(request):
    print('inside assign_ips')
    if request.method == 'POST':

        # Load json data from body
        exam_id = request.data['exam_id']
        exam = Exam.objects.get(id=exam_id)
        print(exam)

        exam_labs = exam.lab_set.all()
        print(exam_labs)

        # exam_lab_ips = exam.lab_set.all()[0].lab_ips.all()
        # print(exam_lab_ips)
        # time_slot_set

        exam_time_slots = Time_Slot.objects.all()
        print(exam_time_slots)

        csv_file = request.FILES['student_list']
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        students_list = list()
        for line in csv.reader(io_string, delimiter=',', quotechar='|'):
            # print(line[0])
            # Looping all and creating student and adding number to students_list
            try:
                split_text = line[0].split(';')
                student_exists = User.objects.filter(username=split_text[2])
            except:
                student_exists = False
            if student_exists:
                print("exists")
                split_text = line[0].split(';')
                students_list.append(split_text[2])
            else:
                user = User()
                # ask prof to send name and dob if need to generate new pass
                profile_data = None
                split_text = line[0].split(';')
                first_name = split_text[0]
                last_name= split_text[1]
                matrikel_number = split_text[2]

                # int_list = list(int_type)

                #password = sum([int(x) for x in matrikel_number])

                password = last_name+matrikel_number
                print("password==",password)
                # print(split_text[1],split_text[0],split_text[2])
                user = User()
                # ask prof to send name and dob if need to generate new pass
                user.set_password(password)
                user.username = matrikel_number
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                students_list.append(line[0])



        random.shuffle(students_list)

        ip_count = 0
        for i in range(len(exam_labs)):
            ip_count = ip_count + len(exam_labs[i].lab_ips.all())

        print(ip_count, len(students_list))
        students_length = len(students_list)
        temp_students_list = students_list
        print("Temps tudent list ",len(temp_students_list))
        # Case 1 when we have more ips and less students

        if ip_count >= students_length:

            each_lab_student_count = students_length/len(exam_labs)
            # we iterate over each lab and assign the students with single time slot

            for i in range(len(exam_labs)):
                exam_lab_ips = exam.lab_set.all()[i].lab_ips.all()
                print(" Number of IPS", len(exam_lab_ips))

                for j in range(len(exam_lab_ips)):
                    if len(temp_students_list) > 0:
                        if j <= each_lab_student_count:
                            print("student username", students_list[0])
                            student_instance = User.objects.get(username=students_list[0])
                            student_instance.ip = exam_lab_ips[j]
                            student_instance.time_slot = exam_time_slots[0]
                            student_instance.exam = exam
                            student_instance.save()
                            temp_students_list.pop(0)

        else:

            # we iterate over each lab and assign the students with single time slot
            for i in range(len(exam_time_slots)):
                print("exam_time_slots", exam_time_slots[i])

                for j in range(len(exam_labs)):
                    exam_lab_ips = exam.lab_set.all()[j].lab_ips.all()

                    for k in range(len(exam_lab_ips)):
                        if len(temp_students_list) > 0:
                            print("student username", students_list[0])
                            student_instance = User.objects.get(username=students_list[0])
                            print("exam_time_slots[i]", exam_time_slots[i])
                            student_instance.ip = exam_lab_ips[k]
                            student_instance.time_slot = exam_time_slots[i]
                            student_instance.exam = exam
                            student_instance.save()
                            temp_students_list.pop(0)


        return JsonResponse({'msg': 'Successfully assigned!', 'success': 1}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'msg': 'Method not allowed!', 'success': 0}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Function based view
@csrf_exempt
@api_view(['POST', ])
# @permission_classes([permissions.IsAdminUser, ])
def de_assign_ips(request):
    print('inside assign_ips')
    if request.method == 'POST':

        # Load json data from body
        parsed_data = json.loads(request.body)

        key = parsed_data.get('key')

        # Fetch all IPs where student is None
        labs = Lab.objects.all()

        lab_ips = LabIp.objects.all()
        # get the counts for students and ips

        #New code

        # for i in range(len(labs)):
        #     current_lab_ips = labs[i].lab_ips.all()
        #     if current_lab_ips is not None:
        #         for current_lab_ip in current_lab_ips:
        #             current_lab_ip.student1 = None
        #             current_lab_ip.student2 = None
        #             # student.timeslot = 1
        #             # student.save()
        #             # save the IP
        #             current_lab_ip.save()

        #Latest code
        exam_id = request.data['exam_id']
        exam = Exam.objects.get(id=exam_id)
        print(exam)

        students = User.objects.filter(exam=exam)

        print(students)

        for i in range(len(students)):
            student_instance = students[i]
            student_instance.ip = None
            student_instance.time_slot = None
            student_instance.exam = None
            student_instance.save()


        # exam_labs = exam.lab_set.all()
        # print(exam_labs)
        # for i in range(len(exam_labs)):
        #         exam_lab_ips = exam.lab_set.all()[i].lab_ips.all()
        #
        #         for j in range(len(exam_lab_ips)):
        #             if len(temp_students_list) > 0:
        #                 print("student username", students_list[0])
        #                 student_instance = User.objects.get(username=students_list[0])
        #                 student_instance.ip = exam_lab_ips[j]
        #                 student_instance.time_slot = exam_time_slots[0]
        #                 student_instance.exam = exam
        #                 student_instance.save()
        #                 temp_students_list.pop(0)

        return JsonResponse({'msg': 'Successfully assigned!', 'success': 1}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'msg': 'Method not allowed!', 'success': 0}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
@api_view(['POST', ])
def assign_single_ip(request):
    print('inside assign single Ip')
    if request.method == 'POST':

        # Load json data from body
        # parsed_data = json.loads(request.body)
        ip_id = request.data['lab_ip_id']
        student_username = request.data['student_username']
        lab_id = request.data['lab_id']
        timeslot_id = request.data['timeslot_id']
        exam_id = request.data['exam_id']
        print("user id ====",student_username)

        student = User.objects.get(username=student_username)
        lab = Lab.objects.get(pk=lab_id)
        labIp = LabIp.objects.get(pk=ip_id)
        timeslot = Time_Slot.objects.get(pk=timeslot_id)
        exam = Exam.objects.get(pk=exam_id)

        student.ip = labIp
        student.time_slot = timeslot
        student.exam = exam
        student.save()

        return JsonResponse({'msg': 'Successfully Assigned!', 'success': 1}, status=status.HTTP_200_OK)

    else:
        return JsonResponse({'msg': 'Method not allowed!', 'success': 0}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



# for student in students: print(student.username, student.exam);
