from django.urls import path

from drfFourViewComponent import views

urlpatterns=[
    path('gx/',views.MyGenericsAndMixins.as_view()),
    path('gx/<str:id>/',views.MyGenericsAndMixins.as_view()),

    path('genmany/',views.MyListAPIView.as_view()),
    path('genone/<str:id>/',views.MyRetrieveAPIView.as_view()),
    path('gencreate/',views.MyCreateAPIView.as_view()),
    path('genupdate/<str:id>/',views.MyUpdateAPIView.as_view()),
    path('gendel/<str:id>/',views.MyDestroyAPIView.as_view()),

    path('viewset/<str:id>/',views.MyViewSets.as_view({'get':'login'})),
    path('viewset/',views.MyViewSets.as_view({'post':'registers'})),


]