from django.contrib import admin
from django.urls import path

from StaleZlecenie import views

urlpatterns = [
   path('standingOrder/', views.CreateStandingOrder.as_view()),
]
