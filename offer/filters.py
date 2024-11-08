import django_filters

from .models import Offer


class OffersFilter(django_filters.FilterSet):
    brokername = django_filters.CharFilter(field_name='broker__name', lookup_expr='icontains')
    parcelname = django_filters.CharFilter(field_name='parcel__name', lookup_expr='icontains')
    
    class Meta:
        model = Offer
        fields = {
            'title':['icontains'],
            'description':['icontains']
        }