from rest_framework import generics

from .models import Offer
from .filters import OffersFilter
from .paginations import OffersPagination
from .serializers import OffersSerializer

# Create your views here.


class CreateListOffers(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    filterset_class = OffersFilter
    pagination_class = OffersPagination
    serializer_class = OffersSerializer
    
    
class OfferDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OffersSerializer