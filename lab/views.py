from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from lab.models import Lab, LabIp, Time_Slot
from lab.serializer import Time_SlotSerializer, LabSerializer
from lab_ip.serializers import LabIpSerializer
import io
import csv
from user.models import User


class LabViewSet(viewsets.ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class LabIpViewSet(viewsets.ModelViewSet):
    queryset = LabIp.objects.all()
    serializer_class = LabIpSerializer

# Function based view

@csrf_exempt
@api_view(['POST', ])
def create_bulk_ips(request):
    print('inside assign_ips')
    if request.method == 'POST':

        # Load json data from body
        # parsed_data = json.loads(request.body)
        room_building = request.data['room_building']
        # to get request args
        print('lab_admin_id==================', request.data)
        if request.data['isNoLabAdmin'] is False:
            lab_admin_id = request.data['lab_admin']
            lab_admin = User.objects.get(pk=lab_admin_id)
            lab = Lab(room_building=room_building, lab_admin=lab_admin)
            lab.save()
            print('lab_admin_id==================', lab_admin_id, room_building)
        else:
            lab = Lab(room_building=room_building)
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


class Time_SlotViewSet(viewsets.ModelViewSet):
    queryset = Time_Slot.objects.all()
    serializer_class = Time_SlotSerializer
