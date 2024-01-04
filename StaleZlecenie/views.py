from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import render
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from Portfel import models as portfel_models
from Portfel.models import Portfel
from StaleZlecenie import models as stale_zlecenie_models
from .models import StaleZlecenie
from .serializer import StaleZlecenieSerializer


class CreateStandingOrder(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        kwota = request.headers.get('money')
        tytul = request.headers.get('title')
        dzienWykonania = request.headers.get('day')
        tokenSTR = request.headers.get('Authorization')
        user = GetUserByToken(tokenSTR)
        portfelDocelowyID = request.headers.get('TargetWalletID')
        portfelDocelowy = portfel_models.Portfel.objects.get(id=portfelDocelowyID)
        portfelZleceniodawcy = portfel_models.Portfel.objects.get(idKlientaUser=user.id)
        zlecenie = stale_zlecenie_models.StaleZlecenie(Kwota=kwota, Tytul=tytul, dzienMiesiaca=dzienWykonania, ID_PortfelaOdbiorcy=portfelDocelowy, ID_PortfelaZleceniodawcy=portfelZleceniodawcy)
        zlecenie.save()
        return Response(status=status.HTTP_201_CREATED)


class GetStandingOrders(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StaleZlecenie.objects.all()
    serializer_class = StaleZlecenieSerializer

    def get(self, request, *args, **kwargs):
        tokenSTR = request.headers.get('Authorization')
        user = GetUserByToken(tokenSTR)
        serializer = StaleZlecenieSerializer(stale_zlecenie_models.StaleZlecenie.objects.filter(ID_PortfelaZleceniodawcy=user.id), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StandingOrderInternal(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StaleZlecenie.objects.all()
    serializer_class = StaleZlecenieSerializer

    def post(self, request, *args, **kwargs):
        tokenSTR = request.headers.get('Authorization')
        user = GetUserByToken(tokenSTR)
        zlecenie = self.get_serializer(data=request.data)
        zlecenie.is_valid(raise_exception=True)
        zlecenie.save(ID_PortfelaZleceniodawcy=Portfel.objects.get(idKlientaUser=user.id))
        return Response(status=status.HTTP_201_CREATED)


class UpdateStandingOrder(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    #TO DO: TESTS!
    def patch(self, request, *args, **kwargs):
        token = request.headers.get('Authorization')
        user = GetUserByToken(token)
        idZlecenia = request.headers.get('orderID')
        if StaleZlecenie.objects.filter(id=idZlecenia, ID_PortfelaZleceniodawcy=user.id).exists():
            if request.headers.get('money') is None:
                kwota = StaleZlecenie.objects.get(id=idZlecenia).Kwota
            else:
                kwota = request.headers.get('money')
            if request.headers.get('title') is None:
                tytul = StaleZlecenie.objects.get(id=idZlecenia).Tytul
            else:
                tytul = request.headers.get('title')
            if request.headers.get('day') is None:
                dzienWykonania = StaleZlecenie.objects.get(id=idZlecenia).dzienMiesiaca
            else:
                dzienWykonania = request.headers.get('day')

            zlecenie = StaleZlecenie.objects.get(id=idZlecenia)
            zlecenie.Kwota = kwota
            zlecenie.Tytul = tytul
            zlecenie.dzienMiesiaca = dzienWykonania
            zlecenie.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        tokenSTR = request.headers.get('Authorization')
        user = GetUserByToken(tokenSTR)
        idZlecenia = request.headers.get('orderID')
        if StaleZlecenie.objects.filter(id=idZlecenia, ID_PortfelaZleceniodawcy=user.id).exists():
            StaleZlecenie.objects.get(id=idZlecenia).delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


def GetUserByToken(token):
    token = token[7:].encode()
    access_token = AccessToken(token)
    user = User.objects.get(id=access_token['user_id'])
    return user
