from django.db import models

#from offer.models import Offer

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
    
    @property
    def offers(self): return self.offer_set.all()
    
    def __str__(self):
        return f"{self.neighborhood} Block {self.block_number} Subdivision {self.subdivision_number}"