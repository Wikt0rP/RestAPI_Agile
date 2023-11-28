from django.db import models


class StaleZlecenie (models.Model):
    dzienMiesiaca = models.IntegerField(0, 31)
    ID_PortfelaZleceniodawcy = models.ForeignKey('Portfel', on_delete=models.CASCADE, related_name='ID_PortfelaZleceniodawcy')
    ID_PortfelaOdbiorcy = models.ForeignKey('Portfel', on_delete=models.CASCADE, related_name='ID_PotrfelaOdbiorcy')
    Kwota = models.DecimalField(max_digits=10, decimal_places=2)
    Tytul = models.CharField(max_length=100, default="StandingOrderNoTitle", null=True)
    ostatniMiesiacWyplaty = models.IntegerField(0, 12, default=None, null=True)
