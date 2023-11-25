from django.db import models
from django.contrib.auth.models import User


class Grupa(models.Model):
    nazwa = models.CharField(max_length=100)
    users = models.ManyToManyField(User)