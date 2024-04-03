from django.test import TestCase
from .models import Destination

class DestinationModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.destination = Destination.objects.create(
            name='Paris',
            country='France',
            description='A Place near Paris to Hangout',
            best_time_to_visit='10:00:00 - 5:00:00',
            category='Test Category',
            image_url='https://www.google.com/imgres?q=paris%20img&imgurl=https%3A%2F%2Ft4.ftcdn.net%2Fjpg%2F02%2F96%2F15%2F35%2F360_F_296153501_B34baBHDkFXbl5RmzxpiOumF4LHGCvAE.jpg&imgrefurl=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dparis&docid=mY-1SM2TnYV90M&tbnid=gfolu93X3mem8M&vet=12ahUKEwi10Lezj6WFAxWB3TgGHaukDGQQM3oECBgQAA..i&w=540&h=360&hcb=2&ved=2ahUKEwi10Lezj6WFAxWB3TgGHaukDGQQM3oECBgQAA'
        )

    def test_destination_creation(self):
        # Test that a Destination object is created correctly
        self.assertEqual(self.destination.name, 'Paris')
        self.assertEqual(self.destination.country, 'France')
        self.assertEqual(self.destination.description, 'A Place near Paris to Hangout')
        self.assertEqual(self.destination.best_time_to_visit, '10:00:00 - 5:00:00')
        self.assertEqual(self.destination.category, 'France')
        self.assertEqual(self.destination.image_url, 'https://www.google.com/imgres?q=paris%20img&imgurl=https%3A%2F%2Ft4.ftcdn.net%2Fjpg%2F02%2F96%2F15%2F35%2F360_F_296153501_B34baBHDkFXbl5RmzxpiOumF4LHGCvAE.jpg&imgrefurl=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dparis&docid=mY-1SM2TnYV90M&tbnid=gfolu93X3mem8M&vet=12ahUKEwi10Lezj6WFAxWB3TgGHaukDGQQM3oECBgQAA..i&w=540&h=360&hcb=2&ved=2ahUKEwi10Lezj6WFAxWB3TgGHaukDGQQM3oECBgQAA')
