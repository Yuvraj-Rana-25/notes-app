from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Note
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class NotesListView(ListView):
    template_name = 'notes.html'
    context_object_name = 'notes'
    model = Note

class NoteDetailView(DetailView):
    template_name = 'note_detail.html'
    context_object_name = 'note'
    model = Note


class NoteCreateView(CreateView):
    template_name = 'note_form.html'
    model = Note
    fields = ['user', 'title', 'content']


class NoteUpdateView(UpdateView):
    template_name = 'note_update.html'
    model = Note
    fields = ['title', 'content']