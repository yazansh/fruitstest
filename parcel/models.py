from django.db import models

# Create your models here.

class LandUseGroup(models.TextChoices):
    AGRICULTURAL = 'Agricultural'
    RESIDENTIAL = 'Residential'
    COMMERCIAL = 'Commercial'


class Parcel(models.Model):
    block_number = models.IntegerField()
    neighberhood = models.TextField()
    subdivision_number = models.IntegerField()
    land_use_group = models.CharField(choices=LandUseGroup.choices)
    description = models.CharField()
    creation_date = models.DateField(auto_now_add=True)