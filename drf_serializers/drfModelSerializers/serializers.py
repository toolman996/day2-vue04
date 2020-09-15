from rest_framework import serializers
from rest_framework import exceptions
from drfSerializer.models import Book, Author, Press


class PressNestedQuery(serializers.ModelSerializer):
    class Meta:
        model=Press
        fields=('press_name','pic_url','address')

#序列化
class MyModelSerializers(serializers.ModelSerializer):
    #嵌套查询
    publish=PressNestedQuery()
    class Meta:
        model=Book
        #查询指定的字段
        fields=('book_name','price','pic_url','publish','authors_name')
        #查询所有字段
        # fields='__all__'
        #不包含查询的字段
        # exclude=('book_name','price','pic')
        #指定查询的深度
        # depth=1

#反序列化
class MyModelDeserializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('book_name','price','publish','authors')

        #添加验证规则
        extra_kwargs={
            'book_name':{
               'max_length':10,
               'min_length':2,
            },
            'publish':{
                'required':True
            }
        }

    #全局钩子校验图书是否存在
    def validate(self, attrs):
        books=attrs.get('book_name')
        result=Book.objects.filter(book_name=books,is_delete=False)
        if result:
            raise exceptions.ValidationError('添加失败，图书已经存在')
        return attrs


#序列化和反序列化结合使用
class Combine(serializers.ModelSerializer):
    # publish = PressNestedQuery()
    class Meta:
        model=Book
        #序列化和反序列化字段的并集
        fields=('book_name','price','publish','authors','pic_url','authors_name')
        extra_kwargs={
            'koob_name':{
                'max_length':10,
                'min_length':2,
            },
            'pic_url':{
                'read_only':True
            },
            'authors':{
                'write_only':True
            },
            'authors_name': {
                'read_only': True
            },
        }

    # def validate(self, attrs):
    #     books=attrs.get('book_name')
    #     result=Book.objects.filter(book_name=books,is_delete=False)
    #     if result:
    #         raise exceptions.ValidationError('添加失败，图书已经存在')
    #     return attrs