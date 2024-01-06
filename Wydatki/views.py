from django.shortcuts import render
from requests import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .models import Wydatki
from .serializer import WydatkiSerializer
from rest_framework import status
from rest_framework.response import Response


class CreateExpense(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WydatkiSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        kwota = request.data['kwota']
        tytul = request.data['tytul']

        wydatki = Wydatki(kwota=kwota, tytul=tytul, idKlientaUser=User.objects.get(id=user.id))
        wydatki.save()
        return Response(status=status.HTTP_201_CREATED)


class ExpenseList(generics.ListAPIView):
    queryset = Wydatki
    serializer_class = WydatkiSerializer

    def get(self, request, *args, **kwargs):
        wydatki = Wydatki.objects.all()
        serializer = WydatkiSerializer(wydatki, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteExpense(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WydatkiSerializer

    def delete(self, request, *args, **kwargs):
        user = request.user
        idWydatku = request.data['id']
        wydatki = Wydatki.objects.get(id=idWydatku, idKlientaUser=User.objects.get(id=user.id))
        wydatki.delete()
        return Response(status=status.HTTP_200_OK)


class ExpenseByUser(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WydatkiSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        wydatki = Wydatki.objects.filter(idKlientaUser=User.objects.get(id=user.id))
        serializer = WydatkiSerializer(wydatki, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)