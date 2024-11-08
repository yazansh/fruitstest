import django_filters

from .models import Parcel

class ParcelsFilter(django_filters.FilterSet):
    
    class Meta:
        model = Parcel
        fields = {
            'block_number': ['exact'],
            'neighborhood': ['icontains'],
            'subdivision_number': ['exact'],
            'land_use_group': ['exact'],
            'description': ['icontains']
            }