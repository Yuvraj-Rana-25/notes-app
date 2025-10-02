from django.shortcuts import render
from rest_framework import generics
from .serializers import NoteSerializer, CommentSerializer
from notes.models import Note, Comment
# Create your views here.

class NotesAPIView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = []


class CommentAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class NoteCommentAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        note_id = self.kwargs['note_id']
        return Comment.objects.filter(note_id=note_id)