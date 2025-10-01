from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from notes.models import Note
# Create your tests here.

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.note = Note.objects.create(title='Test Note', content='This is a test note.', user=CustomUser.objects.create_user(email='d9HtG@example.com', password='testpassword', username='testuser'))
   

    def test_api_list_view(self):
        response = self.client.get(reverse('notes-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Note')
        self.assertEqual(response.data[0]['content'], 'This is a test note.')
