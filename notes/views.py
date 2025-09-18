from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Note
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class NotesListView(ListView):
    template_name = 'notes.html'
    context_object_name = 'notes'
    model = Note