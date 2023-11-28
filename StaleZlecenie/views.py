from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import render
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from Portfel import models


class CreateStandingOrder(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        kwota = request.headers.get('money')
        tytul = request.headers.get('title')
        dzienWykonania = request.headers.get('day')
        tokenSTR = request.headers.get('Authorization')
        user = GetUserByToken(tokenSTR)
        portfelDocelowy = request.headers.get('TargetWalletID')
        portfelZleceniodawcy = models.Portfel.objects.get(idKlientaUser=user.id)



def GetUserByToken(token):
    token = token[7:].encode()
    access_token = AccessToken(token)
    user = User.objects.get(id=access_token['user_id'])
    return user
