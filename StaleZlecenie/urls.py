from django.contrib import admin
from django.urls import path

from StaleZlecenie import views

urlpatterns = [
   path('standingOrder/create', views.CreateStandingOrder.as_view()),
   path('standingOrder/user', views.GetStandingOrders.as_view()),
   path('standingOrder/internal', views.StandingOrderInternal.as_view()),
   path('standingOrder/update', views.UpdateStandingOrder.as_view()),
]
