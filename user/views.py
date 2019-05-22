from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from user.models import User
from user.serializers import UserSerializer,FileSerializer
# Also add these imports
from user.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticatedOrReadOnly,]

class UserListCreateAPIView(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


# FOR UPDATE,FETCH AND DELETE
class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    lookup_field='id'

class StudentsListAPIView(ListAPIView):
    queryset=User.objects.filter(user_type=1)
    serializer_class=UserSerializer
class LabAdminsListAPIView(ListAPIView):
    queryset=User.objects.filter(user_type=3)
    serializer_class=UserSerializer



    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [IsAuthenticatedOrReadOnly]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsAuthenticatedOrReadOnly]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAuthenticatedOrReadOnly]
    #     return [permission() for permission in permission_classes]
