from celery import shared_task
from django.db.models import Count, Q

from parcel.models import Parcel

@shared_task
def monitor_parcel_count():
    # Grouping parcels by block number and subdivision number
    parcel_groups = (
        Parcel.objects
        .values('block_number', 'subdivision_number')
        .annotate(
            total_parcels_count=Count('id'),
            active_parcels_count=Count('id', filter=Q(offer__isnull=False))
        )
    )

    # Checking each group and sending notifications if all parcels are active
    for group in parcel_groups:
        block_number = group['block_number']
        subdivision_number = group['subdivision_number']
        total_parcels_count = group['total_parcels_count']
        active_parcels_count = group['active_parcels_count']

        if active_parcels_count == total_parcels_count:
            send_notification(group)
            

def send_notification(parcel_group):
    print(f"Completed parcels: Block number: {parcel_group['block_number']}, "
                            f"Subdivision number: {parcel_group['subdivision_number']}, "
                            f"Parcel count: {parcel_group['total_parcels_count']}")