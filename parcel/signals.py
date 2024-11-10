from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Parcel

@receiver(post_migrate)
def create_initial_parcels(sender, **kwargs):
    if sender.name == 'parcel' and Parcel.objects.count() == 0:
        print("Seeding Parcel data...")
        parcels_data = [
            {"block_number": 1, "neighborhood": "Neighborhood A", "subdivision_number": 1, "land_use_group": "Residential", "description": "Description for Parcel 1"},
            {"block_number": 1, "neighborhood": "Neighborhood B", "subdivision_number": 1, "land_use_group": "Commercial", "description": "Description for Parcel 2"},
            {"block_number": 1, "neighborhood": "Neighborhood C", "subdivision_number": 2, "land_use_group": "Industrial", "description": "Description for Parcel 3"},
            {"block_number": 2, "neighborhood": "Neighborhood D", "subdivision_number": 2, "land_use_group": "Agricultural", "description": "Description for Parcel 4"},
            {"block_number": 2, "neighborhood": "Neighborhood E", "subdivision_number": 3, "land_use_group": "Residential", "description": "Description for Parcel 5"},
            {"block_number": 2, "neighborhood": "Neighborhood F", "subdivision_number": 3, "land_use_group": "Commercial", "description": "Description for Parcel 6"}
        ]

        for parcel_data in parcels_data:
            Parcel.objects.get_or_create(**parcel_data)

        print("Successfully created initial dummy parcels")
