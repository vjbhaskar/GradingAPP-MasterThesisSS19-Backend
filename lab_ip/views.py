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
            students_list.append(line[0])
        print(students_list)

        random.shuffle(students_list)

        ip_count = 0
        for i in range(len(exam_labs)):
            ip_count = ip_count + len(exam_labs[i].lab_ips.all())

        print(ip_count, len(students_list))
        students_length = len(students_list)
        temp_students_list = students_list
        # Case 1 when we have more ips and less students

        if ip_count >= students_length:

            # we iterate over each lab and assign the students with single time slot

            for i in range(len(exam_labs)):
                exam_lab_ips = exam.lab_set.all()[i].lab_ips.all()

                for j in range(len(exam_lab_ips)):
                    if len(temp_students_list) > 0:
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




        # # Store array of User IDS in Students List
        # students_list = list(parsed_data.get('students'))
        #
        # random.shuffle(students_list)

        # For demo test == get exam ID from request


        # # Fetch all IPs where student is None
        # labs = Lab.objects.all()
        # # labs_labips = labs[0].lab_ips.all()
        #
        # lab_ips = LabIp.objects.all()
        # # get the counts for students and ips
        # students_count = len(students_list)
        # temp_students_list = students_list
        # ip_count = len(lab_ips)
        # print('total ip count===',ip_count)
        #
        # #New code
        #
        # for i in range(len(labs)):
        #     current_lab_ips = labs[i].lab_ips.all()
        #     if current_lab_ips is not None:
        #         for current_lab_ip in current_lab_ips:
        #             temp_std_count = len(temp_students_list)
        #             if temp_std_count > 0:
        #                 print("current_lab_ip,temp_students_list[0]===",current_lab_ip,temp_students_list[0])
        #                 student = User.objects.get(pk=temp_students_list[0])
        #                 current_lab_ip.student1 = student
        #                 student.timeslot = 1
        #                 print("done assigning ip for student 1",temp_students_list)
        #                 temp_students_list.pop(0)
        #                 student.save()
        #                 # save the IP
        #                 current_lab_ip.save()
        #
        # if ip_count < students_count:
        #     for i in range(len(labs)):
        #         current_lab_ips = labs[i].lab_ips.all()
        #         if current_lab_ips is not None:
        #             for current_lab_ip in current_lab_ips:
        #                 temp_std_count = len(temp_students_list)
        #                 if temp_std_count > 0:
        #                     print("current_lab_ip,temp_students_lisct[0]===",current_lab_ip,temp_students_list[0])
        #                     student = User.objects.get(pk=temp_students_list[0])
        #                     current_lab_ip.student2 = student
        #                     student.timeslot = 2
        #                     print("done assigning ip for student 2",temp_students_list)
        #                     temp_students_list.pop(0)
        #                     student.save()
        #                     # save the IP
        #                     current_lab_ip.save()
        # else:
        #     # timeslot 2
        #     return JsonResponse({'msg': 'Not enough IPs Please set time slot', 'success': 0}, status=status.HTTP_400_BAD_REQUEST)

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
