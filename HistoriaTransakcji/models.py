from django.db import models


class HistoriaTransakcji(models.Model):
    ID_PortfelaOdbiorcy = models.ForeignKey('Portfel.Portfel', on_delete=models.CASCADE, related_name='ID_PortfelaOdbiorcy')
    ID_portfelaNadawcy = models.ForeignKey('Portfel.Portfel', on_delete=models.CASCADE, related_name='ID_portfelaNadawcy')
    Kwota = models.IntegerField()
    DataTransakcji = models.DateTimeField()
    Typ = models.CharField(max_length=100)
    Tytul = models.CharField(max_length=100)