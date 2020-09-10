from django.urls import path

from drfapp import views

urlpatterns=[
    # 函数视图定义路由
    path('case/',views.demo),
    # 类视图定义路由
    path('class_view/',views.Case.as_view()),
    path('class_demo/',views.Demo.as_view()),
    path('class_demo/<str:num>/',views.Demo.as_view()),
]