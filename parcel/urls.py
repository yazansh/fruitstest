#from rest_framework.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.CreateListParcels.as_view(), name='create-or-list-parcels'),
    path('<int:pk>', views.ParcelDetails.as_view(), name='get-update-delete-parcel')
]