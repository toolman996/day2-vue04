from django.contrib.auth.models import AbstractUser, User, Permission, Group
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import authentication,permissions,throttling
from drfAuthenticate.authenticator import MyAuth
from drfAuthenticate.permission import MyPermission
from drfAuthenticate.throttle import SendMessageRate
from tool.response import CustomizeResponse


class Case(APIView):
    # authentication_classes = [BasicAuthentication]

    def get(self, request, *args, **kwargs):
        # user = User.objects.first()
        # print(user.email)
        group = Group.objects.first()
        print(group)
        # permission = Permission.objects.first()
        # print(permission.name)
        return Response("OK")

class TestPermissionAPIView(APIView):
    """
    只有认证后的才可以访问
    """
    authentication_classes = [MyAuth]
    permission_classes = [MyPermission]

    def get(self, request, *args, **kwargs):
        return CustomizeResponse("登录访问成功")


class UserLoginOrReadOnly(APIView):
    """
    登录可写  游客只读
    """
    throttle_classes = [UserRateThrottle]

    # permission_classes = [MyPermission]

    def get(self, request, *args, **kwargs):
        return CustomizeResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return CustomizeResponse("写操作")


class SendMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]
    scope='user'
    def get(self, request, *args, **kwargs):
        return CustomizeResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return CustomizeResponse("写操作")












