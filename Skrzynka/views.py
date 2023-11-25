from rest_framework.response import Response
from rest_framework import generics, status
from Skrzynka.models import Skrzynka
from Skrzynka.serializer import SkrzynkaSerializer


class SkrzynkaList(generics.ListCreateAPIView):
    queryset = Skrzynka.objects.all()
    serializer_class = SkrzynkaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SkrzynkaByID(generics.ListCreateAPIView):
    queryset = Skrzynka.objects.all()
    serializer_class = SkrzynkaSerializer

    def get(self, request, *args, **kwargs):
        odbiorcaID = kwargs['odbiorcaID']
        skrzynka = Skrzynka.objects.filter(IDOdbiorcy=odbiorcaID)
        serializer = SkrzynkaSerializer(skrzynka, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SkrzynkaRead(generics.UpdateAPIView):
    queryset = Skrzynka.objects.all()
    serializer_class = SkrzynkaSerializer

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        skrzynka = Skrzynka.objects.get(pk=pk)
        skrzynka.czyPrzeczytane = True
        skrzynka.save()
        serializer = SkrzynkaSerializer(skrzynka)
        return Response(serializer.data, status=status.HTTP_200_OK)


