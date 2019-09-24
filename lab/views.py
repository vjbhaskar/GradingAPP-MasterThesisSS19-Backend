import json
import pprint

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from lab.models import Lab, LabIp, Time_Slot
from lab.serializer import Time_SlotSerializer, LabSerializer
from lab_ip.serializers import LabIpSerializer
from exam.models import Exam
import io
import csv
from user.models import User
from file.models import File
from user.serializers import UserSerializer


class LabViewSet(viewsets.ModelViewSet):

    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class LabIpViewSet(viewsets.ModelViewSet):

    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    queryset = LabIp.objects.all()
    serializer_class = LabIpSerializer

# Function based view

@api_view(['POST', ])
@csrf_exempt
def create_bulk_ips(request):
    print('inside assign_ips')
    if request.method == 'POST':

        # Load json data from body
        # parsed_data = json.loads(request.body)
        room_building = request.data['room_building']
        exam_id = request.data['exam_id']
        exam = Exam.objects.get(pk=exam_id)
        # to get request args
        print('lab_admin_id==================', request.data)
        if request.data['isNoLabAdmin'] == '2':
            lab_admin_id = request.data['lab_admin']
            lab_admin = User.objects.get(pk=lab_admin_id)
            lab = Lab(room_building=room_building, lab_admin=lab_admin, exam=exam)
            lab.save()
            print('lab_admin_id==================', lab_admin_id, room_building)
        else:
            lab = Lab(room_building=room_building, exam=exam)
            lab.save()

        if request.FILES:
            csv_file = request.FILES['ip_list']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            print('lab---', lab)
            for line in csv.reader(io_string, delimiter=',', quotechar='|'):
                print(line[0])
                lab_ip = LabIp(ip=line[0], lab=lab)
                lab_ip.save()
            # handel error here
        return JsonResponse({'msg': 'Successfully Created!', 'success': 1}, status=status.HTTP_201_CREATED)

    else:
        return JsonResponse({'msg': 'Method not allowed!', 'success': 0}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
@api_view(['POST', ])
def fetch_lab_assigned_students(request):
    if request.method == 'POST':

        username = request.data['username']
        user = User.objects.get(username=username)
        lab = Lab.objects.filter(lab_admin=user).get()
        if lab:
            print("lab is not empty")
            lab_ips = lab.lab_ips.all()
            lab_ips_list = [x.id for x in lab_ips]

            users = User.objects.raw('SELECT * FROM user_user WHERE ip_id in %s' % (tuple(lab_ips_list),))

            data = []
            for user in users:
                file = File.objects.filter(user=user).all()
                file_list = [request.build_absolute_uri(x.file_obj.url) for x in file]
                file_ids = [x.id for x in file]
                file_names = [x.name for x in file]
                data.append({
                    'username': user.username,
                    'ip': user.ip.ip,
                    'login': user.login_ip,
                    'file': file_list,
                    'file_ids': file_ids,
                    'file_names': file_names
                })

            pprint.pprint(data)
        else:
            print("lab is empty")
            return JsonResponse({'msg': 'No lab assigned', 'success': 0}, status=status.HTTP_404_NOT_FOUND)

        # See it json functions
        # data = json.dumps(data, ensure_ascii=False, indent=2)

        if users:
            return JsonResponse({'msg': 'success', 'success': 1, 'data': data}, status=status.HTTP_200_OK)

    else:
        return JsonResponse({'msg': 'Method not allowed!', 'success': 0}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class Time_SlotViewSet(viewsets.ModelViewSet):

    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    queryset = Time_Slot.objects.all()
    serializer_class = Time_SlotSerializer
