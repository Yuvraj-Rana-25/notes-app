from django.shortcuts import render
from rest_framework import generics
from .serializers import NoteSerializer
from notes.models import Note
# Create your views here.

class NotesAPIView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer