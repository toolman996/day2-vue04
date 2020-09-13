from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

# @csrf_protect为视图开启csrf认证
from drfapp.models import Message


@csrf_exempt  #为函数视图免除csrf认证
def demo(request):# 函数视图
    if request.method=='GET':
        print(request.GET.get('name'))
        return HttpResponse('%s'%request.GET.get('name'))
    if request.method=='POST':
        print(request.POST.get('name'))
        return HttpResponse('SSSSSS')
    if request.method=='PUT':
        print(request.GET.get('name'))
        return HttpResponse('DSAA')
    if request.method=='DELETE':
        print('DELETE')
        return HttpResponse('DELETE方法触发')
    if request.method=='UPDATE':
        print('UPDATE')
        return HttpResponse('UPDATE方法触发')


# @method_decorator(csrf_protect,name='dispatch') 为类视图开启csrf认证
@method_decorator(csrf_exempt,name='dispatch')  #为类视图免除csrf认证
class Case(View):# 类视图
    def get(self,request,*args,**kwargs):
        print('get方法')
        return HttpResponse('get ok')
    def post(self,request,*args,**kwargs):
        print('post方法')
        return HttpResponse('post ok')
    def put(self,request,*args,**kwargs):
        print('put方法')
        return HttpResponse('put ok')
    def delete(self,request,*args,**kwargs):
        print('delete方法')
        return HttpResponse('delete ok')

@method_decorator(csrf_exempt,name='dispatch')
class Demo(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('num')
        if id:
            result=Message.objects.filter(id=id).values().first()
            if result:
                return JsonResponse({
                    'status':200,
                    'msg':'查询单个信息成功',
                    'value':result
                })
            else:
                return JsonResponse({
                    'status': 500,
                    'msg': '查询单个信息失败',
                })
        else:
            result=Message.objects.all().values()
            print(result)
            if result:
                return JsonResponse({
                    'status': 200,
                    'msg': '查询全部信息成功',
                    'value': list(result)
                })
            # else:
            #     return JsonResponse({
            #         'status': 500,
            #         'msg': '查询全部信息失败',
            #     })

        return JsonResponse({
            'status':500,
            'msg':'查询的数据不存在'

            })

    def post(self, request, *args, **kwargs):
        name=request.POST.get('name')
        age=request.POST.get('age')
        try:
            Message.objects.create(name=name,age=age)
            return JsonResponse({
                'status':200,
                'msg':'创建成功',
                'value':{'name':name,'age':age}
            })
        except:
            return JsonResponse({
                'status': 500,
                'msg': '创建失败',
            })

class Bt(APIView):
    def get(self,request,*args,**kwargs):
        id=request.query_params.get('num')
        if id:
            result=Message.objects.filter(id=id).values().first()
            if result:
                return JsonResponse({
                    'status':200,
                    'msg':'查询单个信息成功',
                    'value':result
                })
            else:
                return JsonResponse({
                    'status': 500,
                    'msg': '查询单个信息失败',
                })
        else:
            result=Message.objects.all().values()
            print(result)
            if result:
                return JsonResponse({
                    'status': 200,
                    'msg': '查询全部信息成功',
                    'value': list(result)
                })
            # else:
            #     return JsonResponse({
            #         'status': 500,
            #         'msg': '查询全部信息失败',
            #     })

        return JsonResponse({
            'status':500,
            'msg':'查询的数据不存在'

            })

    def post(self, request, *args, **kwargs):
        name=request.data.get('name')
        age=request.data.get('age')
        try:
            Message.objects.create(name=name,age=age)
            return JsonResponse({
                'status':200,
                'msg':'创建成功',
                'value':{'name':name,'age':age}
            })
        except:
            return JsonResponse({
                'status': 500,
                'msg': '创建失败',
            })




















