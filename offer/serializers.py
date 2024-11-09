from rest_framework import serializers
from .models import Offer
from parcel.models import Parcel

class OffersSerializer(serializers.ModelSerializer):
    parcels = serializers.PrimaryKeyRelatedField(queryset=Parcel.objects.all(), many=True)

    class Meta:
        model = Offer
        fields = ['id', 'title', 'description', 'broker', 'price_per_meter', 'parcels', 'creation_date', 'last_update_date']

    def create(self, validated_data):
        parcels_data = validated_data.pop('parcels')
        
        invalid_parcels = []
        for parcel in parcels_data:
            if not Parcel.objects.filter(id=parcel.id).exists():
                invalid_parcels.append(parcel.id)

        if invalid_parcels:
            raise serializers.ValidationError(f"Invalid parcel IDs: {invalid_parcels}")

        offer = Offer.objects.create(**validated_data)

        offer.parcels.set(parcels_data)
        return offer
