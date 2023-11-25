from django.db import models


class CeleOszczednosciowe (models.Model):
    cel = models.CharField(max_length=100)
    kwotaUzbierana = models.DecimalField(max_digits=10, decimal_places=2)
    kwotaCel = models.DecimalField(max_digits=10, decimal_places=2)
    IDPorfela = models.ForeignKey('Portfel.Portfel', on_delete=models.CASCADE)
