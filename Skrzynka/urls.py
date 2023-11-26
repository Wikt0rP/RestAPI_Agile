from django.contrib import admin
from django.urls import path
from Skrzynka import views

urlpatterns = [
    path('skrzynka/', views.SkrzynkaList.as_view()),
    path('skrzynka/userid=<odbiorcaID>', views.SkrzynkaByID.as_view()),
    path('skrzynka/read/<pk>', views.SkrzynkaRead.as_view()),

]
