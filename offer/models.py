from django.db import models

from broker.models import Broker
from parcel.models import Parcel

# Create your models here.


class Offer(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=300, default='', blank=True)
    broker = models.ForeignKey(Broker, null=False, on_delete=models.CASCADE)
    parcels = models.ManyToManyField(Parcel)
    price_per_meter = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)