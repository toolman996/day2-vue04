from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission



class MyPermission(BasePermission):

    def has_permission(self, request, view):
        # 如果是只读接口  则所有人都可以访问
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        username = request.data.get("username")
        # 如果用户访问时写操作 判断用户是否有登录信息
        user = User.objects.filter(username=username).first()
        if user:
            return True
        return False
