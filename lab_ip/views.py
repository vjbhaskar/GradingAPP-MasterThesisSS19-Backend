import json
import random
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import UpdateAPIView
from lab.models import LabIp,Lab
from .serializers import LabIpStudentSerializer

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
        parsed_data = json.loads(request.body)
        print("students===========",parsed_data)

        # Store array of User IDS in Students List
        students_list = list(parsed_data.get('students'))

        random.shuffle(students_list)

        # Fetch all IPs where student is None
        labs = Lab.objects.all()
        # labs_labips = labs[0].lab_ips.all()

        lab_ips = LabIp.objects.all()
        # get the counts for students and ips
        students_count = len(students_list)
        temp_students_list = students_list
        ip_count = len(lab_ips)
        print('total ip count===',ip_count)

        #New code

        for i in range(len(labs)):
            current_lab_ips = labs[i].lab_ips.all()
            if current_lab_ips is not None:
                for current_lab_ip in current_lab_ips:
                    temp_std_count = len(temp_students_list)
                    if temp_std_count > 0:
                        print("current_lab_ip,temp_students_list[0]===",current_lab_ip,temp_students_list[0])
                        student = User.objects.get(pk=temp_students_list[0])
                        current_lab_ip.student1 = student
                        student.timeslot = 1
                        print("done assigning ip for student 1",temp_students_list)
                        temp_students_list.pop(0)
                        student.save()
                        # save the IP
                        current_lab_ip.save()

        if ip_count < students_count:
            for i in range(len(labs)):
                current_lab_ips = labs[i].lab_ips.all()
                if current_lab_ips is not None:
                    for current_lab_ip in current_lab_ips:
                        temp_std_count = len(temp_students_list)
                        if temp_std_count > 0:
                            print("current_lab_ip,temp_students_lisct[0]===",current_lab_ip,temp_students_list[0])
                            student = User.objects.get(pk=temp_students_list[0])
                            current_lab_ip.student2 = student
                            student.timeslot = 2
                            print("done assigning ip for student 2",temp_students_list)
                            temp_students_list.pop(0)
                            student.save()
                            # save the IP
                            current_lab_ip.save()
        else:
            # timeslot 2
            return JsonResponse({'msg': 'Not enough IPs Please set time slot', 'success': 0}, status=status.HTTP_400_BAD_REQUEST)

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

        for i in range(len(labs)):
            current_lab_ips = labs[i].lab_ips.all()
            if current_lab_ips is not None:
                for current_lab_ip in current_lab_ips:
                    current_lab_ip.student1 = None
                    current_lab_ip.student2 = None
                    # student.timeslot = 1
                    # student.save()
                    # save the IP
                    current_lab_ip.save()

        return JsonResponse({'msg': 'Successfully assigned!', 'success': 1}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'msg': 'Method not allowed!', 'success': 0}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
