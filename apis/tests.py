from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from notes.models import Note, Comment
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

    def test_api_detail_view(self):
        response = self.client.get(reverse('api-note-detail', args=[self.note.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Note')
        self.assertEqual(response.data['content'], 'This is a test note.')

    
class CommentAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(email='d9HtG@example.com', password='testpassword', username='testuser')
        cls.note = Note.objects.create(title='Test Note', content='This is a test note.', user=cls.user)
        cls.comment = Comment.objects.create(note=cls.note, content='This is a test comment.', user=cls.user)

    def test_comment_api_list_view(self):
        response = self.client.get(reverse('comment-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], 'This is a test comment.')

    def test_comment_detail_api(self):
        response = self.client.get(reverse('comment-detail', args=[self.comment.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], 'This is a test comment.')

    def test_note_comment_api(self):
        response = self.client.get(reverse('note-comment', args=[self.note.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], 'This is a test comment.')