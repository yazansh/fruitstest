
from django.urls import path

from . import views

urlpatterns = [
 path('', views.CreateListOffers.as_view(), name='list-create-offer'),
 path('<int:pk>', views.OfferDetails.as_view(), name='retrieve-update-delete-offer')
]