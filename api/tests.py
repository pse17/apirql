from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User(username='admin')
        return super().setUp()
    
    def test_username(self):
        self.assertEqual(self.user.username, 'admin')

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.response = self.client.post(
            reverse('create'),
            {'username': 'user1'},
            format='json'
        )
        return super().setUp()

    def test_api_can_create_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

