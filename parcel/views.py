from django.shortcuts import render
from rest_framework import generics

from parcel.models import Parcel
from parcel.paginations import ParcelsPagination
from parcel.serializers import ParcelsSerializer
from parcel.filters import ParcelsFilter

# Create your views here.


class CreateListParcels(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelsSerializer
    pagination_class = ParcelsPagination
    filterset_class = ParcelsFilter
    
    
class ParcelDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelsSerializer