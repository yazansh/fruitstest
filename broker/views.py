from django.shortcuts import render
from rest_framework import generics

from .models import Broker
from .paginations import BrokersPagination
from .filters import BrokersFilter
from .serializers import BrokersSerializer

# Create your views here.


class CreateListBrokers(generics.ListCreateAPIView):
    queryset = Broker.objects.all()
    pagination_class = BrokersPagination
    filterset_class = BrokersFilter
    serializer_class = BrokersSerializer
    
    
class BrokerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokersSerializer