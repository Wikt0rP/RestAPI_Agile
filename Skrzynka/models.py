from django.db import models
from django.contrib.auth.models import User


class Skrzynka (models.Model):
    temat = models.CharField(max_length=100)
    tresc = models.TextField()
    czyPrzeczytane = models.BooleanField()
    IDOdbiorcy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='odbiorcy')
    IDNadawcy = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='nadawcy')
