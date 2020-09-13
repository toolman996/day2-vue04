from rest_framework.response import Response
from rest_framework.views import exception_handler as fun
from rest_framework import status


def exception_handler(exc, context):
    # 打印错误信息
    error = "%s %s %s" % (context['view'], context['request'].method, exc)
    print(error)

    #调用drf封装好的函数如果返回为none执行下面操作
    result = fun(exc, context)
    if result is None:
        return Response(
            {"error_msg": "工作人员正在处理中，请稍等。。。"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=None)

    # 返回值不为空直接返回即可
    return result
