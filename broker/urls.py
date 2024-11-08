from django.urls import path

from . import views

urlpatterns = [
 path('', views.CreateListBrokers.as_view(), name='create-list-brokers'),
 path('<int:pk>', views.BrokerDetails.as_view(), name='get-update-delete-broker')
]