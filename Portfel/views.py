import requests
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import Portfel.models as models
import Portfel.serializer as PorfteSerializer


class CreateWallet(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            user_id = request.headers['Userid']
            print(request.headers)
            portfel = models.Portfel.objects.get(idKlientaUser=user_id)
            if portfel is not None:
                print(f"Portfel dla {user_id} juz istnieje")
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                portfel = models.Portfel(idKlientaUser=user_id)
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