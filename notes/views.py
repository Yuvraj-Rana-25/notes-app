from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

class NotesListView(LoginRequiredMixin,ListView):
    template_name = 'notes.html'
    context_object_name = 'notes'
    model = Note
    login_url = 'login'

class NoteDetailView(LoginRequiredMixin, DetailView):
    template_name = 'note_detail.html'
    context_object_name = 'note'
    model = Note
    login_url = 'login'


class NoteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'note_form.html'
    model = Note
    fields = ['title', 'content']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'note_update.html'
    model = Note
    fields = ['title', 'content']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'note_delete.html'
    model = Note
    success_url = reverse_lazy('notes')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)