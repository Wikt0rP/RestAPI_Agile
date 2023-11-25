from django.contrib import admin
from django.urls import path

from CeleOszczednosciowe import views

urlpatterns = [
    path('savings/', views.CeleOszczednoscioweList.as_view()),
    path('savings/id=<int:pk>/', views.CeleOszczednoscioweDetail.as_view()),
    path('savings/walletID=<int:walletID>/', views.CeleOszczednoscioweDetail2.as_view()),

    path('savings/update/id=<int:pk>/add=<int:value>/', views.CeleOszczednoscioweAdd.as_view()),
    path('savings/update/id=<int:pk>/remove=<int:value>/', views.CeleOszczednoscioweRemove.as_view()),
]
