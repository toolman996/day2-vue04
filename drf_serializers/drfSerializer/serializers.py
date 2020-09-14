from rest_framework import serializers, exceptions, status
from rest_framework.response import Response

from drfSerializer.models import MyModel
from drf_serializers import settings

#序列化
class MySerializers(serializers.Serializer):
    name = serializers.CharField()
    pwd = serializers.CharField()
    age = serializers.CharField()

    # 自定义字段 图片
    img=serializers.SerializerMethodField()
    #自定义字段 性别
    sex=serializers.SerializerMethodField()

    #定义方法获取值
    def get_sex(self,obj):
        #choices类型才能使用:get_字段名_display()获取对应的值
        return obj.get_sex_display()

    # 定义方法返回图片的url
    def get_img(self,obj):
        return 'http://127.0.0.1:8000'+'%s'%settings.MEDIA_URL+'%s'%obj.img

#反序列化
class MyDeSerializers(serializers.Serializer):
    name = serializers.CharField(
        #定义字段校验规则
        max_length=4,min_length=2,
        error_messages={
            'max_length':'名字太长不合法',
            'min_length':'名字太短不合法',
        }
    )
    pwd = serializers.CharField()
    age = serializers.CharField()


    again_pwd=serializers.CharField()
    #局部钩子
    def validate_name(self, value):
        return value
    #全局钩子
    def validate(self, attrs):
        print(attrs)
        password=attrs.get('pwd')
        again_password=attrs.pop('again_pwd')
        print(again_password)
        if password!=again_password:
            print('11111')
            # raise exceptions.ValidationError('11111')
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'msg':'密码输入不正确，请重新输入。。。'
            })
        return attrs



    #serializers没有实现create方法在保存时需要重写才能实现添加数据
    def create(self, validated_data):
        return MyModel.objects.create(**validated_data)