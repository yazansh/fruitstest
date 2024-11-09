from rest_framework import serializers

from .models import Parcel
from offer.serializers import OffersSerializer

class ParcelsSerializer(serializers.ModelSerializer):
    offers = OffersSerializer(many=True, read_only=True)
    
    class Meta:
        model = Parcel
        fields = ['id', 'block_number', 'neighborhood', 'subdivision_number', 'land_use_group', 'description', 'creation_date', 'offers']