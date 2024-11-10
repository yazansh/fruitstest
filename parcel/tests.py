from django.test import TestCase
from .models import Parcel

class ParcelModelTest(TestCase):
    def setUp(self):
        self.parcel = Parcel.objects.create(
            block_number=1,
            neighborhood="Downtown",
            subdivision_number=2,
            land_use_group='Residential',
            description="A residential parcel"
        )

    def test_parcel_creation(self):
        self.assertEqual(self.parcel.block_number, 1)
        self.assertEqual(self.parcel.neighborhood, "Downtown")
        self.assertEqual(self.parcel.subdivision_number, 2)
        self.assertEqual(self.parcel.land_use_group, 'Residential')
        self.assertEqual(self.parcel.description, "A residential parcel")
    
    def test_parcel_str(self):
        self.assertEqual(str(self.parcel), "Downtown Block 1 Subdivision 2")