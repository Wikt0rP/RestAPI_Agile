from django.contrib import admin
from django.urls import path

from Portfel import views

urlpatterns = [
    path('wallet/create/', views.CreateWallet.as_view()),
    path('wallets/', views.WalletList.as_view()),
    path('sendtransfer/', views.SendTransfer.as_view()),
    path('wallet/user/', views.GetWalletByUser.as_view()),
    path('wallet/add/', views.AddWallet.as_view()),



]
