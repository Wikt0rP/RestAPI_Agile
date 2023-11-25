from django.db import models


class StaleZlecenie (models.Model):
    Data = models.DateField()
    ID_PortfelaZleceniodawcy = models.IntegerField()
    ID_PortfelaZleceniobiorcy = models.IntegerField()
    Kwota = models.DecimalField(max_digits=10, decimal_places=2)

