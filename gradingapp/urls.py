"""gradingapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from rest_framework.routers import DefaultRouter

# from lab.views import Time_SlotViewSet
from lab_ip.views import assign_ips
from lab_ip.views import de_assign_ips
from lab_ip.views import assign_single_ip
from user import views as user_views
from file import views as file_views
from subject import views as subject_views
from lab import views as lab_views
from exam import views as exam_views
from user.views import get_user_ip

router=DefaultRouter()
router.register('users',user_views.UserViewSet)
router.register('subject',subject_views.SubjectViewSet)
router.register('lab',lab_views.LabViewSet)
router.register('labIp',lab_views.LabIpViewSet)
router.register('timeSlot',lab_views.Time_SlotViewSet)
router.register('exam',exam_views.ExamViewSet)
urlpatterns = [

    url(r'api/',include(router.urls)),
    url(r'api/assign_students/', assign_ips),
    url(r'api/de_assign_students/', de_assign_ips),
    url(r'^admin/', admin.site.urls),
    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),
    url(r'^api/user/$', user_views.UserListCreateAPIView.as_view()),
    url(r'^api/user/students/$', user_views.StudentsListAPIView.as_view()),
    url(r'^api/user/labadmins/$', user_views.LabAdminsListAPIView.as_view()),
    url(r'^api/user/(?P<id>[0-9a-f-]+)/$', user_views.UserRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^api/file/$', file_views.FileListCreateAPIView.as_view()),
    url(r'^api/file/(?P<id>\d+)/$', file_views.FileRetrieveUpdateDestroyAPIView.as_view()),
    url(r'api/user/bulkstudents', user_views.create_user),
    url(r'api/labIp/bulk', lab_views.create_bulk_ips),
    url(r'api/labIp/adminips', lab_views.fetch_lab_assigned_students),
    url(r'api/assign_single_ip/', assign_single_ip),
    url(r'api/getIp/', get_user_ip)


    # url(r'^api/assignstudents/$',lab_ip_views.LabIpUpdateAPIView.as_view()),
]
#
