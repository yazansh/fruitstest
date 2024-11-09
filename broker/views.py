from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Broker
from .paginations import BrokersPagination
from .filters import BrokersFilter
from .serializers import BrokersSerializer

# Create your views here.


class CreateListBrokers(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Broker.objects.all()
    pagination_class = BrokersPagination
    filterset_class = BrokersFilter
    serializer_class = BrokersSerializer
    
    
class BrokerDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Broker.objects.all()
    serializer_class = BrokersSerializer