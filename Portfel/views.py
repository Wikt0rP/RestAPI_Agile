from datetime import datetime
from decimal import Decimal

import requests
from django.db import transaction
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from HistoriaTransakcji.models import HistoriaTransakcji
import Portfel.models as models
from .serializer import PortfelSerializer
from django.contrib.auth.models import User
from .models import Portfel


class CreateWallet(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            tokenStr = request.headers['Authorization']
            user = GetUserByToken(tokenStr)
            portfel = None
            try:
                portfel = Portfel.objects.get(idKlientaUser=user.id)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            except:
                if portfel is not None:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    portfel = Portfel(idKlientaUser=User.objects.get(id=user.id), idKlientaGrupa=None, kwota=0)
                    portfel.save()
                    return Response(status=status.HTTP_201_CREATED)

        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class WalletList(generics.ListAPIView):
    queryset = Portfel
    serializer_class = PortfelSerializer

    def get(self, request, *args, **kwargs):
        portfel = Portfel.objects.all()
        serializer = PortfelSerializer(portfel, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SendTransfer(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PortfelSerializer

    def post(self, request, *args, **kwargs):
        try:
            tokenStr = request.headers['Authorization']
            user = GetUserByToken(tokenStr)
            portfel = Portfel.objects.get(idKlientaUser=user.id)
            docelowyPortfel = Portfel.objects.get(id=request.headers['Targetwallet'])
            pieniadze = Decimal(request.headers['Money'])

            with transaction.atomic():
                docelowyPortfel.kwota += pieniadze
                portfel.kwota -= pieniadze
                docelowyPortfel.save()
                portfel.save()
                historia = HistoriaTransakcji(ID_portfelaNadawcy=portfel, ID_PortfelaOdbiorcy=docelowyPortfel, Kwota=pieniadze, Typ="Przelew", Tytul="Przelew z portfela", DataTransakcji=datetime.now())
                historia.save()
                return Response(status=status.HTTP_200_OK)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetWalletByUser(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PortfelSerializer

    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            portfel = Portfel.objects.get(idKlientaUser=user.id)
            serializer = PortfelSerializer(portfel, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def GetUserByToken(token):
    token = token[7:].encode()
    access_token = AccessToken(token)
    user = User.objects.get(id=access_token['user_id'])
    return user

