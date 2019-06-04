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
        ip_count = len(lab_ips)

        # ips should always be equal or greater than number of students
        if ip_count >= students_count:
            # loop over students list
            # when to replace New students with assigned students


            for k in range(len(labs)):
                print(labs[k].lab_ips.all())
                current_lab_ips = labs[k].lab_ips.all()
                for current_lab_ip in current_lab_ips:
                    print(current_lab_ip)
                # get labs and loop through number of IPs
                # check if lab has empty IPs
                # assign IPS to students
                pass

            for i in range(len(students_list)):
                # get the student at index i
                student = User.objects.get(pk=students_list[i])

                # get the ip at index i of lab
                lab = labs[i].lab_ips.all()

                # print('Lab Ips Count = ', labs[i].lab_count())
                print('in loop lab==', lab)
                if lab is not None:
                    for ip in lab:
                        print ('in loop ip==',ip.pk)
                        # assign the student to index `i` IP
                        ip_instance = LabIp.objects.get(pk=ip.pk)
                        if ip.student1 is not None:
                            ip.student1 = student
                            student.timeslot = 1

                        # student.save()

                        # save the IP
                        # ip.save()
        else:
            # timeslot 2
            return JsonResponse({'msg': 'Not enough IPs Please set time slot', 'success': 0}, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({'msg': 'Successfully assigned!', 'success': 1}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'msg': 'Method not allowed!', 'success': 0}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
