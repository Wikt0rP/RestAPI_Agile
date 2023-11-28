from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import render
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from Portfel import models as portfel_models
from StaleZlecenie import models as stale_zlecenie_models
import StaleZlecenie.serializer as StaleZlecenieSerializer
from StaleZlecenie.serializer import StaleZleceniaSerializer


# TO DO: sprawdzic czy dziala
# TO DO: sprawdzic czy dziala
# TO DO: sprawdzic czy dziala
# TO DO: sprawdzic czy dziala

class CreateStandingOrder(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        kwota = request.headers.get('money')
        tytul = request.headers.get('title')
        dzienWykonania = request.headers.get('day')
        tokenSTR = request.headers.get('Authorization')
        user = GetUserByToken(tokenSTR)
        portfelDocelowy = request.headers.get('TargetWalletID')
        portfelZleceniodawcy = portfel_models.Portfel.objects.get(idKlientaUser=user.id)
        zlecenie = stale_zlecenie_models.StaleZlecenie(Kwota=kwota, Tytul=tytul, dzienMiesiaca=dzienWykonania, ID_PortfelaOdbiorcy=portfelDocelowy, ID_PortfelaZleceniodawcy=portfelZleceniodawcy)
        zlecenie.save()
        return Response(status=status.HTTP_201_CREATED)


class GetStandingOrders(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = stale_zlecenie_models.StaleZlecenie.objects.all()
    serializer_class = StaleZlecenieSerializer.StaleZleceniaSerializer

    def get(self, request, *args, **kwargs):
        tokenSTR = request.headers.get('Authorization')
        user = GetUserByToken(tokenSTR)
        serializer = StaleZlecenieSerializer.StaleZleceniaSerializer(stale_zlecenie_models.StaleZlecenie.objects.filter(idPortfeluZleceniodawcy=user.id), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StandingOrderInternal(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = stale_zlecenie_models.StaleZlecenie.objects.all()
    serializer_class = StaleZlecenieSerializer.StaleZleceniaSerializer

    def get(self, request, *args, **kwargs):
        tokenSTR = request.headers.get('Authorization')
        user = GetUserByToken(tokenSTR)
        kwota = request.headers.get('money')
        tytul = request.headers.get('title')
        portfel = portfel_models.Portfel.objects.get(idKlientaUser=user.id)
        dzienWykonania = request.headers.get('day')
        zlecenie = stale_zlecenie_models.StaleZlecenie(Kwota=kwota, Tytul=tytul, ID_PortfelaZleceniodawcy=portfel, ID_PortfelaOdbiorcy=portfel, dzienMiesiaca=dzienWykonania)
        zlecenie.save()
        return Response(status=status.HTTP_201_CREATED)

def GetUserByToken(token):
    token = token[7:].encode()
    access_token = AccessToken(token)
    user = User.objects.get(id=access_token['user_id'])
    return user
