from django.db import models
from django.contrib.auth.models import User
from Grupa.models import Grupa


class Wydatki(models.Model):
    kwota = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    idKlientaUser = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    idKlientaGrupa = models.ForeignKey(Grupa, on_delete=models.CASCADE, null=True, blank=True)
    tytul = models.CharField(max_length=100, null=True, blank=True)