from rest_framework import serializers

from .models import Parcel

class ParcelsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parcel
        fields = "__all__"