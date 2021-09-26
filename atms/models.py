from enum import unique
import uuid
from django.db import models
from django.contrib.auth.models import User
import pickle

# Create your models here.
with open('static/files/currencies.pkl','rb') as file:
    CHOICES = pickle.load(file)

CHOICES = list(CHOICES)

class Atm(models.Model):
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    country = models.CharField(max_length=50)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    in_currency = models.CharField(max_length=50,choices=CHOICES)
    out_currency = models.CharField(max_length=5)
