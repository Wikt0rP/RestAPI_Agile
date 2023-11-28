from django.contrib import admin
from django.urls import path
from User import views

urlpatterns = [
   path('getuser/', views.GetUserByToken.as_view()),
]
