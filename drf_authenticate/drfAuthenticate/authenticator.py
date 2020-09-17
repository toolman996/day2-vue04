from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions




class MyAuth(BaseAuthentication):

    def authenticate(self, request):
        # 获取认证信息
        auth = request.META.get("HTTP_AUTHORIZATION", None)

        if auth is None:
            # 代表没有认证信息  游客
            return None

        # 设置认证信息的校验
        auth_list = auth.split()

        # 校验规则：认证信息的格式是否符合要求
        if not (len(auth_list) == 2 and auth_list[0].lower() == "auth"):
            raise exceptions.APIException("用户认证信息格式有误")

        # 如果认证成功，则解析用户  暂时规定认证信息必须是`tom.abc.123`
        if auth_list[1] != "com.www.123":
            raise exceptions.APIException("用户信息校验失败")

        # 校验数据库是否存在此用户
        user = User.objects.filter(username="admin").first()

        if not user:
            raise exceptions.APIException("用户不存在")

        return (user, None)
