from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drfSerializer.models import MyModel
from drfSerializer.serializers import MySerializers, MyDeSerializers


class MyApiview(APIView):
    # 查询接口api
    def get(self,request,*args,**kwargs):
        number=kwargs.get('num')
        if number:
            result=MyModel.objects.get(id=number)
            return Response({
                'status':status.HTTP_200_OK,
                'msg':'查询成功',
                'value':MySerializers(result).data,
            })
        else:
            result = MyModel.objects.all()
            return Response({
                'status': status.HTTP_200_OK,
                'msg': '查询成功',
                'value': MySerializers(result,many=True).data,
            })

    #增加接口api
    def post(self,request,*args,**kwargs):
        data_dict=request.data
        if not isinstance(data_dict,dict) or data_dict == {}:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'msg':'请求数据类型错误',
            })
        result=MyDeSerializers(data=data_dict)
        #判断是否符合校验规则
        if result.is_valid():
            obj=result.save()
            return Response({
                'status':status.HTTP_200_OK,
                'msg':'添加用户成功',
                'value':MySerializers(obj).data
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': '保存失败',
        })