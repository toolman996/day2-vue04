from django.urls import path

from drfAuthenticate import views

urlpatterns=[
    path('rbac/',views.Case.as_view()),
    path('per/',views.TestPermissionAPIView.as_view()),
    path('auth/',views.UserLoginOrReadOnly.as_view()),
    path('thr/',views.SendMessageAPIView.as_view()),
]