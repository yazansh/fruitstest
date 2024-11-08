import django_filters

from .models import Broker


class BrokersFilter(django_filters.FilterSet):
    
    class Meta:
        model = Broker
        fields = {
            'name': ['icontains'],
            'type': ['exact'],
            'phone_number': ['icontains'],
            'address': ['icontains']
        }