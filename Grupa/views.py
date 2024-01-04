from django.db import transaction
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

import User
from Grupa.models import Grupa
from Grupa.serializer import GroupSerializer
from Portfel.models import Portfel
from django.contrib.auth.models import User


class GrupaCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        tokenStr = request.headers['Authorization']
        user = GetUserByToken(tokenStr)
        grupa = Grupa(nazwa=request.headers['nazwa'], adminGrupy=user)

        portfel = Portfel(idKlientaGrupa=grupa, idKlientaUser=None)
        with transaction.atomic():
            grupa.save()
            grupa.users.set([user])
            grupa.save()
            portfel.save()
            return Response(request.data, status=status.HTTP_201_CREATED)


class GrupaList(generics.ListCreateAPIView):
    queryset = Grupa.objects.all()
    serializer_class = GroupSerializer

    def post(self, request, *args, **kwargs):
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


def GetUserByToken(token):
    token = token[7:].encode()
    access_token = AccessToken(token)
    user = User.objects.get(id=access_token['user_id'])
    return user
