from django.db import models


class Skrzynka (models.Model):
    temat = models.CharField(max_length=100)
    data = models.DateTimeField()
    tresc = models.TextField()
    czyPrzeczytane = models.BooleanField()
    IDOdbiorcy = models.IntegerField()
    IDNadawcy = models.IntegerField()
