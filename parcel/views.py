from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from parcel.models import Parcel
from parcel.paginations import ParcelsPagination
from parcel.serializers import ParcelsSerializer
from parcel.filters import ParcelsFilter

# Create your views here.


class CreateListParcels(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Parcel.objects.all()
    serializer_class = ParcelsSerializer
    pagination_class = ParcelsPagination
    filterset_class = ParcelsFilter
    
class ParcelDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Parcel.objects.all()
    serializer_class = ParcelsSerializer