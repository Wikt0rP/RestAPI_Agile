from django.views.generic import DetailView
from rest_framework import generics, status
from rest_framework.response import Response

from HistoriaTransakcji.models import HistoriaTransakcji
from HistoriaTransakcji.serializer import HistoriaTransakcjiSerializer


class HistoriaTransakcjiList(generics.ListCreateAPIView):

    queryset = HistoriaTransakcji.objects.all()
    serializer_class = HistoriaTransakcjiSerializer

    def post(self, request, *args, **kwargs):
        historia = self.get_serializer(data=request.data)
        historia.is_valid(raise_exception=True)
        historia.save()
        return Response(historia.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        historia = self.get_serializer(HistoriaTransakcji.objects.all(), many=True)
        return Response(historia.data, status=status.HTTP_200_OK)


class HistoriaTransakcjiDetail(generics.ListAPIView):

    serializer_class = HistoriaTransakcjiSerializer
    queryset = HistoriaTransakcji.objects.all()

    def get(self, request, *args, **kwargs):
        historia = self.get_serializer(HistoriaTransakcji.objects.filter(pk=kwargs['pk']), many=True)
        return Response(historia.data, status=status.HTTP_200_OK)


class HistoriaTransakcjiPortfelDetail(generics.ListAPIView):

    serializer_class = HistoriaTransakcjiSerializer
    queryset = HistoriaTransakcji.objects.all()

    def get(self, request, *args, **kwargs):
        historia = self.get_serializer(HistoriaTransakcji.objects.filter(ID_Portfela=kwargs['pk']), many=True)
        return Response(historia.data, status=status.HTTP_200_OK)
