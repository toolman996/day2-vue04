from rest_framework import viewsets
from rest_framework import generics
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin
from rest_framework import views

from drfFourViewComponent.serializers import Combine
from drfSerializer.models import Book
from tool.response import CustomizeResponse

#继承generics和mixins组件实现接口开发
class MyGenericsAndMixins(generics.GenericAPIView,ListModelMixin,DestroyModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin):
    #提供指定的模型数据
    queryset = Book.objects.filter(is_delete=False)
    #提供序列化器
    serializer_class = Combine
    #指定参数名
    lookup_field = 'id'

    def get(self,request,*args,**kwargs):
        if kwargs.get('id'):
            result=self.retrieve(request,*args,**kwargs)
            return CustomizeResponse(data_message='查询成功',results=result.data)
        else:
            result = self.list(request, *args, **kwargs)
            return CustomizeResponse(data_message='查询成功', results=result.data)

    def post(self,request,*args,**kwargs):
        result=self.create(request,*args,**kwargs)
        return CustomizeResponse(data_message='添加成功', results=result.data)

    def put(self,request,*args,**kwargs):
        result = self.update(request, *args, **kwargs)
        return CustomizeResponse(data_message='单个整体修改成功', results=result.data)

    def delete(self,request,*args,**kwargs):
        self.destroy(request, *args, **kwargs)
        return CustomizeResponse(data_message='删除成功')

    def patch(self,request,*args,**kwargs):
        result = self.partial_update(request, *args, **kwargs)
        return CustomizeResponse(data_message='单个局部修改成功', results=result.data)

class MyRetrieveAPIView(generics.RetrieveAPIView):
    # 提供指定的模型数据
    queryset = Book.objects.filter(is_delete=False)
    # 提供序列化器
    serializer_class = Combine
    # 指定参数名
    lookup_field = 'id'

class MyListAPIView(generics.ListAPIView):
    # 提供指定的模型数据
    queryset = Book.objects.filter(is_delete=False)
    # 提供序列化器
    serializer_class = Combine

class MyCreateAPIView(generics.CreateAPIView):
    # 提供指定的模型数据
    queryset = Book.objects.filter(is_delete=False)
    # 提供序列化器
    serializer_class = Combine

class MyUpdateAPIView(generics.UpdateAPIView):
    # 提供指定的模型数据
    queryset = Book.objects.filter(is_delete=False)
    # 提供序列化器
    serializer_class = Combine
    # 指定参数名
    lookup_field = 'id'

class MyDestroyAPIView(generics.DestroyAPIView):
    # 提供指定的模型数据
    queryset = Book.objects.filter(is_delete=False)
    # 提供序列化器
    serializer_class = Combine
    # 指定参数名
    lookup_field = 'id'

class MyViewSets(viewsets.ModelViewSet):
    # 提供指定的模型数据
    queryset = Book.objects.filter(is_delete=False)
    # 提供序列化器
    serializer_class = Combine
    # 指定参数名
    lookup_field = 'id'

    def login(self,request,*args,**kwargs):
        self.retrieve(request,*args,**kwargs)
        return CustomizeResponse(data_message='登录成功')
    def registers(self,request,*args,**kwargs):
        result=self.create(request,*args,**kwargs)
        return CustomizeResponse(data_message='注册成功',results=result.data)























