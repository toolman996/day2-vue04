from django.urls import path

from drfModelSerializers import views

urlpatterns=[
    path('modelser/',views.MyModelApiview.as_view()),
    path('modelser/<str:num>/',views.MyModelApiview.as_view()),

    path('rwser/',views.CombineApiview.as_view()),
    path('rwser/<str:num>/',views.CombineApiview.as_view()),
]