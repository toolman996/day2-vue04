from django.urls import path

from drfSerializer import views

urlpatterns=[
    path('ser/',views.MyApiview.as_view()),
    path('ser/<str:num>/',views.MyApiview.as_view())
]