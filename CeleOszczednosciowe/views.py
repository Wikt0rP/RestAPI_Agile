from rest_framework import generics, status
from rest_framework.response import Response

import CeleOszczednosciowe
from CeleOszczednosciowe.models import CeleOszczednosciowe
from CeleOszczednosciowe.serializer import CeleOszczednoscioweSerializer


class CeleOszczednoscioweList(generics.ListCreateAPIView):

    queryset = CeleOszczednosciowe.objects.all()
    serializer_class = CeleOszczednoscioweSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        cele = self.get_serializer(data=request.data)
        cele.is_valid(raise_exception=True)
        cele.save()
        return Response(cele.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        cele = self.get_serializer(CeleOszczednosciowe.objects.all(), many=True)
        return Response(cele.data, status=status.HTTP_200_OK)


class CeleOszczednoscioweDetail(generics.ListAPIView):

    serializer_class = CeleOszczednoscioweSerializer
    queryset = CeleOszczednosciowe.objects.all()

    def get(self, request, *args, **kwargs):
        cele = self.get_serializer(CeleOszczednosciowe.objects.filter(pk=kwargs['pk']), many=True)
        return Response(cele.data, status=status.HTTP_200_OK)


class CeleOszczednoscioweDetail2(generics.ListAPIView):

    serializer_class = CeleOszczednoscioweSerializer
    queryset = CeleOszczednosciowe.objects.all()

    def get(self, request, *args, **kwargs):
        historia = self.get_serializer(CeleOszczednosciowe.objects.filter(IDPorfela=kwargs['walletID']), many=True)
        return Response(historia.data, status=status.HTTP_200_OK)


class CeleOszczednoscioweAdd(generics.UpdateAPIView):
    serializer_class = CeleOszczednoscioweSerializer
    queryset = CeleOszczednosciowe.objects.all()

    def put(self, request, *args, **kwargs):
        cele = CeleOszczednosciowe.objects.get(pk=kwargs['pk'])
        cele.kwotaUzbierana = cele.kwotaUzbierana + kwargs['value']
        cele.save()
        return Response(status=status.HTTP_200_OK)


class CeleOszczednoscioweRemove(generics.UpdateAPIView):
    serializer_class = CeleOszczednoscioweSerializer
    queryset = CeleOszczednosciowe.objects.all()

    def put(self, request, *args, **kwargs):
        cele = CeleOszczednosciowe.objects.get(pk=kwargs['pk'])
        cele.kwotaUzbierana = cele.kwotaUzbierana - kwargs['value']
        cele.save()
        return Response(status=status.HTTP_200_OK)