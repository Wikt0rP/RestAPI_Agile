from django.contrib import admin
from django.urls import path
from Skrzynka import views

urlpatterns = [
    path('mail/', views.SkrzynkaList.as_view()),
    path('mail/userid=<odbiorcaID>', views.SkrzynkaByID.as_view()),
    path('mail/read/<pk>', views.SkrzynkaRead.as_view()),

]
