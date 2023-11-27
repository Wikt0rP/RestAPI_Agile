from rest_framework import generics, status
from rest_framework.response import Response

import User
from Grupa.models import Grupa
from Grupa.serializer import GroupSerializer
from Portfel.models import Portfel
from django.contrib.auth.models import User


class GrupaList(generics.ListCreateAPIView):
    queryset = Grupa.objects.all()
    serializer_class = GroupSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        grupa = self.get_serializer(data=request.data)
        grupa.is_valid(raise_exception=True)
        grupa.save()
        portfel = Portfel(idKlientaGrupa=grupa.instance, idKlientaUser=None)
        portfel.save()
        return Response(request.data, status=status.HTTP_201_CREATED)


class GrupaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grupa.objects.all()
    serializer_class = GroupSerializer

    def get(self, request, *args, **kwargs):
        grupa = Grupa.objects.filter(users__id=kwargs['pk'])

        serializer = GroupSerializer(grupa, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GrupaAddUser(generics.UpdateAPIView):
    queryset = Grupa.objects.all()
    serializer_class = GroupSerializer

    def put(self, request, *args, **kwargs):
        try:
            grupa = Grupa.objects.get(id=kwargs['id_grupy'])
            user = User.objects.get(id=kwargs['id_uzytkownika'])
            grupa.users.add(user)
            grupa.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GrupaDeleteUser(generics.UpdateAPIView):
    queryset = Grupa.objects.all()
    serializer_class = GroupSerializer

    def put(self, request, *args, **kwargs):

        try:
            grupa = Grupa.objects.get(id=kwargs['id_grupy'])
            user = User.objects.get(id=kwargs['id_uzytkownika'])
            grupa.users.remove(user)
            grupa.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

