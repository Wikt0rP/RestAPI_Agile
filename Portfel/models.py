from django.db import models

from Grupa.models import Grupa


class Portfel(models.Model):

    kwota = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    idKlienta = models.ForeignKey(Grupa, on_delete=models.CASCADE)
