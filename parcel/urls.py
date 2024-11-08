#from rest_framework.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path('parcels/', views.CreateListParcels.as_view(), name='create-or-list-parcels')
]