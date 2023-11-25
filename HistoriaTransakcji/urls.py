from django.contrib import admin
from django.urls import path

from HistoriaTransakcji import views

urlpatterns = [
    path('history/', views.HistoriaTransakcjiList.as_view()),
    path('history/transactionID=<int:pk>/', views.HistoriaTransakcjiDetail.as_view()),
    path('history/walletID=<int:pk>/', views.HistoriaTransakcjiPortfelDetail.as_view()),


]
