from django.db import models
from django.contrib.auth.models import User


class Grupa(models.Model):
    nazwa = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='users')
    adminGrupy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adminGrupy')