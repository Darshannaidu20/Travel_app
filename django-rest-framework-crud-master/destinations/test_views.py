from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Destination
from .serializers import DestinationSerializer

class DestinationAPIViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123',password2 = 'password123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.destination = Destination.objects.create(
            name='Paris',
            country='France',
            description='A Place near Paris to Hangout',
            best_time_to_visit='10:00:00 - 5:00:00',
            category='Test Category',
            image_url='https://www.google.com/imgres?q=paris%20img&imgurl=https%3A%2F%2Ft4.ftcdn.net%2Fjpg%2F02%2F96%2F15%2F35%2F360_F_296153501_B34baBHDkFXbl5RmzxpiOumF4LHGCvAE.jpg&imgrefurl=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dparis&docid=mY-1SM2TnYV90M&tbnid=gfolu93X3mem8M&vet=12ahUKEwi10Lezj6WFAxWB3TgGHaukDGQQM3oECBgQAA..i&w=540&h=360&hcb=2&ved=2ahUKEwi10Lezj6WFAxWB3TgGHaukDGQQM3oECBgQAA',
            creator=self.user
        )

    def test_list_destinations(self):
        url = reverse('destination-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_destination(self):
        url = reverse('destination-list-create')
        data = {
            'name': 'Paris',
            'country': 'France',
            'description': 'A Place near Paris to Hangout',
            'best_time_to_visit': '10:00:00 - 5:00:00',
            'category': 'New Category',
            'image_url': 'https://www.google.com/imgres?q=paris%20img&imgurl=https%3A%2F%2Ft4.ftcdn.net%2Fjpg%2F02%2F96%2F15%2F35%2F360_F_296153501_B34baBHDkFXbl5RmzxpiOumF4LHGCvAE.jpg&imgrefurl=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dparis&docid=mY-1SM2TnYV90M&tbnid=gfolu93X3mem8M&vet=12ahUKEwi10Lezj6WFAxWB3TgGHaukDGQQM3oECBgQAA..i&w=540&h=360&hcb=2&ved=2ahUKEwi10Lezj6WFAxWB3TgGHaukDGQQM3oECBgQAA'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Destination.objects.count(), 2)  # Ensure a new destination was created

    def test_retrieve_destination(self):
        url = reverse('destination-detail', args=[self.destination.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.destination.name)

    def test_update_destination(self):
        url = reverse('destination-detail', args=[self.destination.id])
        data = {'name': 'Updated Destination'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Destination.objects.get(id=self.destination.id).name, 'Updated Destination')

    def test_delete_destination(self):
        url = reverse('destination-detail', args=[self.destination.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Destination.objects.count(), 0)  # Ensure destination was deleted
