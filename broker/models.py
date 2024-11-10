
from django.db import models


# Create your models here.

class BrokerType(models.TextChoices):
    PERSONAL = 'Personal'
    COMPANY = 'Company'
    GOVERNMENTAL = 'Governmental'

class Broker(models.Model):
    name = models.CharField(max_length=100, blank=False)
    type = models.CharField(max_length=50, choices=BrokerType.choices)
    phone_number = models.CharField(max_length=25, default='', blank=True)
    email = models.CharField(max_length=100, blank=False)
    address = models.TextField(max_length=500, default='', blank=True)
    bio = models.CharField(max_length=200, default='', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email