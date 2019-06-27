import json

from rest_framework import viewsets
from user.models import User, UserProfile
from user.serializers import UserSerializer
# Also add these imports
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import io
import csv


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def retrieve(self, request, *args, **kwargs):
        print('inside retrieve!')
        client_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        print(client_ip)
        if client_ip:
            client_ip = client_ip.split(',')[0]
        else:
            client_ip = request.META.get('REMOTE_ADDR')
        print(client_ip)
        user_instance = User
        serializer = UserSerializer(User.objects.all(), request)
        # print(serializer.initial_data)
        if serializer.is_valid():

            print(serializer.data)
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BulkStudentAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Function based view

@csrf_exempt
@api_view(['POST', ])
# @permission_classes([permissions.IsAdminUser, ])
def create_user(request):
    print('inside assign_ips')
    if request.method == 'POST':

        # Load json data from body
        # parsed_data = json.loads(request.body)
        print("students===========", request.FILES)
        csv_file = request.FILES['user_list']
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        for line in csv.reader(io_string, delimiter=',', quotechar='|'):
            print(line[0], line[1])
            profile_data = None
            user = User()
            # ask prof to send name and dob if need to generate new pass
            user.set_password(line[1])
            user.username = line[0]
            user.save()
            # UserProfile.objects.create(user=user, profile=profile_data)
            # handel error here
        return JsonResponse({'msg': 'Successfully Created!', 'success': 1}, status=status.HTTP_201_CREATED)

    else:
        return JsonResponse({'msg': 'Method not allowed!', 'success': 0}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
@api_view(['POST', ])
# @permission_classes([permissions.IsAdminUser, ])
def get_user_ip(request):
    print('inside assign_ips')
    if request.method == 'POST':
        print('inside retrieve!')
        client_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        user_name = request.data['username']
        user = User.objects.get(username=user_name)

        print(client_ip)
        if client_ip:
            client_ip = client_ip.split(',')[0]
            user.login_ip = client_ip
            user.save()

        else:
            client_ip = request.META.get('REMOTE_ADDR')
            user.login_ip = client_ip
            user.save()
        print(client_ip)
        return JsonResponse({'msg': 'Success!', 'success': 1, 'data': client_ip}, status=status.HTTP_201_CREATED)

    else:
        return JsonResponse({'msg': 'Method not allowed!', 'success': 0}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# FOR UPDATE,FETCH AND DELETE
class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class StudentsListAPIView(ListAPIView):
    queryset = User.objects.filter(user_type=1)
    serializer_class = UserSerializer


class LabAdminsListAPIView(ListAPIView):
    queryset = User.objects.filter(user_type=3)
    serializer_class = UserSerializer



    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [IsAuthenticatedOrReadOnly]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsAuthenticatedOrReadOnly]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAuthenticatedOrReadOnly]
    #     return [permission() for permission in permission_classes]
