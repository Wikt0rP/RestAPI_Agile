from django.db import models


class HistoriaTransakcji(models.Model):
    ID_Portfela = models.ForeignKey('Portfel.Portfel', on_delete=models.CASCADE)
    Kwota = models.IntegerField()
    DataTransakcji = models.DateTimeField()
    Typ = models.CharField(max_length=100)