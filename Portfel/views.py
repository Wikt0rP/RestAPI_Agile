from contextvars import Token
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
import Portfel.serializer as PorfteSerializer
from django.contrib.auth.models import User


class CreateWallet(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            tokenStr = request.headers['Authorization']
            user = GetUserByToken(tokenStr)
            portfel = None
            try:
                portfel = models.Portfel.objects.get(idKlientaUser=user.id)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            except:
                if portfel is not None:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    portfel = models.Portfel(idKlientaUser=User.objects.get(id=user.id), idKlientaGrupa=None, kwota=0)
                    portfel.save()
                    return Response(status=status.HTTP_201_CREATED)

        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class WalletList(generics.ListAPIView):
    queryset = models.Portfel.objects.all()
    serializer_class = PorfteSerializer.PortfelSerializer

    def get(self, request, *args, **kwargs):
        portfel = models.Portfel.objects.all()
        serializer = PorfteSerializer.PortfelSerializer(portfel, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SendTransfer(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PorfteSerializer.PortfelSerializer

    def put(self, request, *args, **kwargs):
        try:
            tokenStr = request.headers['Authorization']
            user = GetUserByToken(tokenStr)
            portfel = models.Portfel.objects.get(idKlientaUser=user.id)
            docelowyPortfel = models.Portfel.objects.get(id=request.headers['Targetwallet'])
            pieniadze = Decimal(request.headers['Money'])

            with transaction.atomic():
                docelowyPortfel.kwota += pieniadze
                portfel.kwota -= pieniadze
                docelowyPortfel.save()
                portfel.save()
                historia = HistoriaTransakcji(ID_portfelaNadawcy=portfel, ID_PortfelaOdbiorcy=docelowyPortfel, Kwota=pieniadze, Typ="Przelew", Tytul="Przelew z portfela", DataTransakcji=datetime.now())
                historia.save()
                return Response(status=status.HTTP_200_OK)

        except models.Portfel.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError as e:
            return Response({f"message: Nie znaleziono klucza {str(e)} w żądaniu."}, status=status.HTTP_400_BAD_REQUEST)


def GetUserByToken(token):
    token = token[7:].encode()
    access_token = AccessToken(token)
    user = User.objects.get(id=access_token['user_id'])
    return user

