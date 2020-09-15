from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drfSerializer.models import Book
from drfModelSerializers.serializers import MyModelSerializers, MyModelDeserializers, Combine


class MyModelApiview(APIView):
    # 查询接口api
    def get(self,request,*args,**kwargs):
        number=kwargs.get('num')
        if number:
            result=Book.objects.get(id=number,is_delete=False)
            return Response({
                'status':status.HTTP_200_OK,
                'msg':'查询成功',
                'value':MyModelSerializers(result).data,
            })
        else:
            result = Book.objects.filter(is_delete=False)
            return Response({
                'status': status.HTTP_200_OK,
                'msg': '查询成功',
                'value': MyModelSerializers(result,many=True).data,
            })

    #增加接口api
    def post(self,request,*args,**kwargs):
        data_dict=request.data
        # print(data_dict)
        if not isinstance(data_dict,dict) or data_dict == {}:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'msg':'请求数据类型错误',
            })
        result=MyModelDeserializers(data=data_dict)
        # print(result)
        #判断是否符合校验规则
        result.is_valid(raise_exception=True)
        # if result.is_valid():
        obj=result.save()
        return Response({
            'status':status.HTTP_200_OK,
            'msg':'添加用户成功',
            'value':MyModelSerializers(obj).data
        })
        # return Response({
        #     'status': status.HTTP_400_BAD_REQUEST,
        #     'msg': '保存失败',
        # })

#序列化与反序列化整合类
class CombineApiview(APIView):
    # 查询接口api
    def get(self,request,*args,**kwargs):
        number=kwargs.get('num')
        if number:
            result=Book.objects.get(id=number,is_delete=False)
            return Response({
                'status':status.HTTP_200_OK,
                'msg':'查询成功',
                'value':Combine(result).data,
            })
        else:
            result = Book.objects.filter(is_delete=False)
            return Response({
                'status': status.HTTP_200_OK,
                'msg': '查询成功',
                'value': Combine(result,many=True).data,
            })

    #增加接口api
    def post(self,request,*args,**kwargs):
        data_dict=request.data

        # if not isinstance(data_dict,dict) or data_dict == {} or not isinstance(data_dict,list) or data_dict == []:
        #     return Response({
        #         'status':status.HTTP_400_BAD_REQUEST,
        #         'msg':'请求数据类型错误',
        #     })
        if isinstance(data_dict,dict) and data_dict != {}:
            many=False
        elif isinstance(data_dict,list) and data_dict !=[]:
            many=True
        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '请求数据类型错误',
            })

        result=Combine(data=data_dict,many=many)
        #判断是否符合校验规则
        result.is_valid(raise_exception=True)
        obj=result.save()
        return Response({
            'status':status.HTTP_200_OK,
            'msg':'添加书籍成功',
            'value':Combine(obj,many=many).data
        })

    #删除接口
    def delete(self, request, *args, **kwargs):
        number=kwargs.get('num')
        if number:
            id=[number]
        else:
            id=request.data.get('num')
        result=Book.objects.filter(id__in=id,is_delete=False).update(is_delete=True)
        if result:
            return Response({
                'status':status.HTTP_200_OK,
                'msg':'删除成功'
            })
        return Response({
            'status': status.HTTP_200_OK,
            'msg': '删除失败'
        })

    #更新整体单个
    def put(self, request, *args, **kwargs):
        id=kwargs.get('num')

        all_data=request.data
        try:
            book_obj=Book.objects.get(id=id)
        except:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'msg':'书籍不存在,无法完成修改'
            })
        result=Combine(data=all_data,instance=book_obj)
        result.is_valid(raise_exception=True)
        value=result.save()
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': '修改成功',
            'value':Combine(value).data
        })

    #更新局部单个
    def patch(self, request, *args, **kwargs):
        id=kwargs.get('num')

        all_data=request.data
        try:
            book_obj=Book.objects.get(id=id)
        except:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'msg':'书籍不存在,无法完成修改'
            })
        #更新整体单个和更新局部单个的区别在于 指定 partial=True
        result=Combine(data=all_data,instance=book_obj,partial=True)
        result.is_valid(raise_exception=True)
        value=result.save()
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': '修改成功',
            'value':Combine(value).data
        })
