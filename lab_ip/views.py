import json
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import UpdateAPIView
from lab.models import LabIp
from .serializers import LabIpStudentSerializer

User = get_user_model()


# Create your views here.
class LabIpUpdateAPIView(UpdateAPIView):
    queryset = LabIp.objects.all()
    serializer_class = LabIpStudentSerializer


@csrf_exempt
@api_view(['POST', ])
@permission_classes([permissions.IsAdminUser, ])
def assign_ips(request):
    if request.method == 'POST':
        # Load json data from body
        students = json.loads(request.body)

        # Store array of User IDS in Students List
        students_list = list(students.get('students'))

        # Fetch all IPs where student is None
        lab_ips = LabIp.objects.filter(student=None)

        # get the counts for students and ips
        students_count = len(students_list)
        ip_count = len(lab_ips)

        # ips should always be equal or greater than number of students
        if ip_count >= students_count:
            # loop over students list
            for i in range(len(students_list)):
                # get the student at index i
                student = User.objects.get(pk=students_list[i])

                # get the ip at index i
                ip = LabIp.objects.get(pk=lab_ips[i].pk)

                # assign the student to index `i` IP
                ip.student = student

                # save the IP
                ip.save()
        else:
             return JsonResponse({'msg': 'Not enough free IPs', 'success': 0}, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({'msg': 'Successfully assigned!', 'success': 1}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'msg': 'Method not allowed!', 'success': 0}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
