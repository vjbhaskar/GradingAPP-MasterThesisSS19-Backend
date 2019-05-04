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
from user import views as user_views
from file import views as file_views
router=DefaultRouter()
router.register('users',user_views.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth-jwt/',obtain_jwt_token),
    url(r'^auth-jwt-refresh/',refresh_jwt_token),
    url(r'^auth-jwt-verify/',verify_jwt_token),
    #url(r'',include(router.urls)),
    #url(r'^api/', include('user.urls')),
    url(r'^api/user/$',user_views.UserListCreateAPIView.as_view()),
    url(r'^api/user/(?P<id>\d+)/$',user_views.UserRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^api/file/$',file_views.FileListCreateAPIView.as_view()),
    url(r'^api/file/(?P<id>\d+)/$',file_views.FileRetrieveUpdateDestroyAPIView.as_view())
]
#
