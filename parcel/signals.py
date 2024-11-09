from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Parcel

@receiver(post_migrate)
def create_initial_parcels(sender, **kwargs):
    if sender.name == 'your_app_name':
        parcels_data = [
            {"name": "Parcel 1", "block_number": 101, "neighborhood": "Neighborhood A", "subdivision_number": 1, "land_use_group": "Residential", "description": "Description for Parcel 1"},
            {"name": "Parcel 2", "block_number": 101, "neighborhood": "Neighborhood B", "subdivision_number": 1, "land_use_group": "Commercial", "description": "Description for Parcel 2"},
            {"name": "Parcel 3", "block_number": 101, "neighborhood": "Neighborhood C", "subdivision_number": 2, "land_use_group": "Industrial", "description": "Description for Parcel 3"},
            {"name": "Parcel 4", "block_number": 102, "neighborhood": "Neighborhood D", "subdivision_number": 2, "land_use_group": "Agricultural", "description": "Description for Parcel 4"},
            {"name": "Parcel 5", "block_number": 102, "neighborhood": "Neighborhood E", "subdivision_number": 3, "land_use_group": "Residential", "description": "Description for Parcel 5"},
            {"name": "Parcel 6", "block_number": 102, "neighborhood": "Neighborhood F", "subdivision_number": 3, "land_use_group": "Commercial", "description": "Description for Parcel 6"}
        ]

        for parcel_data in parcels_data:
            Parcel.objects.get_or_create(**parcel_data)

        print("Successfully created initial dummy parcels")
