from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class Fabrics(models):
    name = models.CharField(max_length=128)
