from rest_framework import serializers

from .models import Broker

class BrokersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Broker
        fields = '__all__'