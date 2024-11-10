from django.test import TestCase
from datetime import date

from .models import Parcel, Offer, Broker

class OfferModelTest(TestCase):
    def setUp(self):
        self.current_date = date.today()
        self.broker = Broker.objects.create(
            name="Test Broker",
            type="Company",
            email="broker@test.com"
        )
        self.parcel = Parcel.objects.create(
            block_number=1,
            neighborhood="Downtown",
            subdivision_number=2,
            land_use_group='Residential',
            description="A residential parcel"
        )
        self.offer = Offer.objects.create(
            title="Special Offer",
            description="A special offer description",
            broker=self.broker,
            price_per_meter=100.00,
        )
        self.offer.parcels.add(self.parcel)

    def test_offer_creation_date(self):
        self.assertEqual(self.offer.creation_date, self.current_date)

    def test_offer_creation(self):
        self.assertEqual(self.offer.title, "Special Offer")
        self.assertEqual(self.offer.description, "A special offer description")
        self.assertEqual(self.offer.broker.name, "Test Broker")
        self.assertEqual(self.offer.price_per_meter, 100.00)
        self.assertIn(self.parcel, self.offer.parcels.all())

    def test_offer_str(self):
        self.assertEqual(str(self.offer), "Special Offer")
