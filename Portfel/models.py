from django.db import models
from Grupa.models import Grupa
from django.contrib.auth.models import User


class Portfel(models.Model):
    kwota = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    idKlientaUser = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    idKlientaGrupa = models.ForeignKey(Grupa, on_delete=models.CASCADE, null=True, blank=True)
