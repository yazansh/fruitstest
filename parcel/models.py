from django.db import models

# Create your models here.

class LandUseGroup(models.TextChoices):
    AGRICULTURAL = 'Agricultural'
    RESIDENTIAL = 'Residential'
    COMMERCIAL = 'Commercial'


class Parcel(models.Model):
    block_number = models.IntegerField()
    neighborhood = models.TextField(max_length=1000, default='', blank=True)
    subdivision_number = models.IntegerField()
    land_use_group = models.CharField(max_length=100, choices=LandUseGroup.choices)
    description = models.CharField(max_length=200, default='', blank=True)
    creation_date = models.DateField(auto_now_add=True)