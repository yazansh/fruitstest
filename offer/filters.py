import django_filters
from django_filters import BaseInFilter, NumberFilter

from .models import Offer


class NumberInFilter(BaseInFilter, NumberFilter):
    pass

class OffersFilter(django_filters.FilterSet):
    broker = django_filters.NumberFilter(field_name='broker__id')
    parcels = NumberInFilter(field_name='parcels__id', lookup_expr='in')
    
    class Meta:
        model = Offer
        fields = {
            'title':['icontains'],
            'description':['icontains'],
            'broker': ['exact'],
            'parcels': ['in']
        }