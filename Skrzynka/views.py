from django.shortcuts import render
from requests import Response
from rest_framework import generics, status

from Skrzynka.models import Skrzynka
from Skrzynka.serializer import SkrzynkaSerializer


class SkrzynkaList(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        skrzynka = Skrzynka.objects.all()
        serializer = SkrzynkaSerializer(skrzynka, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SkrzynkaByID(generics.RetrieveAPIView):
    queryset = Skrzynka.objects.all()
    serializer_class = SkrzynkaSerializer

    def get(self, request, *args, **kwargs):
        odbiorcaID = kwargs['odbiorcaID']
        skrzynka = Skrzynka.objects.filter(IDOdbiorcy=odbiorcaID)
        serializer = SkrzynkaSerializer(skrzynka, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

