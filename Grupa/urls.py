from django.contrib import admin
from django.urls import path

from Grupa import views

urlpatterns = [
    path('group/', views.GrupaList.as_view()),
    path('group/create/', views.GrupaCreate.as_view()),
    path('group/user=<int:pk>/', views.GrupaDetail.as_view()),
    path('group=<id_grupy>/adduser=<id_uzytkownika>', views.GrupaAddUser.as_view()),
    path('group=<id_grupy>/deleteuser=<id_uzytkownika>', views.GrupaDeleteUser.as_view()),
]
