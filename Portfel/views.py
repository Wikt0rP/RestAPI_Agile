from datetime import datetime
from decimal import Decimal

import requests
from django.db import transaction
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from unicodedata import decimal
from HistoriaTransakcji.models import HistoriaTransakcji
from rest_framework.authentication import TokenAuthentication
import Portfel.models as models
import Portfel.serializer as PorfteSerializer
from django.contrib.auth.models import User


class CreateWallet(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            user_id = request.headers['Userid']
            user = User.objects.get(id=user_id)
            print(request.headers)
            portfel = None
            try:
                portfel = models.Portfel.objects.get(idKlientaUser=user)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            except:
                if portfel is not None:
                    print(f"Portfel dla {user_id} juz istnieje")
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    portfel = models.Portfel(idKlientaUser=User.objects.get(id=user_id), idKlientaGrupa=None, kwota=0)
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
            portfel = models.Portfel.objects.get(idKlientaUser=request.headers['Userid'])
            docelowyPortfel = models.Portfel.objects.get(id=request.headers['Targetwallet'])
            pieniadze = Decimal(request.headers['Money'])

            print(f"Przelew z {portfel.id} do {docelowyPortfel.id} w kwocie {pieniadze}")
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
