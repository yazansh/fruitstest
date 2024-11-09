from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Offer
from .filters import OffersFilter
from .paginations import OffersPagination
from .serializers import OffersSerializer

# Create your views here.


class CreateListOffers(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Offer.objects.all().order_by('-id')
    filterset_class = OffersFilter
    pagination_class = OffersPagination
    serializer_class = OffersSerializer
    
class OfferDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Offer.objects.all()
    serializer_class = OffersSerializer