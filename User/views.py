from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth.models import User

from Grupa.models import Grupa

permission_classes = (IsAuthenticated,)


class GetUserByToken(generics.GenericAPIView):

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        try:
            untyped_token = UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.get(id=untyped_token['user_id'])
        groups = Grupa.objects.filter(users__id=user.id)
        group_names = [group.nazwa for group in groups]
        return Response({"user_id": user.id, "username": user.username, "email": user.email, "groups": group_names},
                        status=status.HTTP_200_OK)

