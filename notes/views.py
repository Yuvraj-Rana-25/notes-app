from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Note, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsListView(LoginRequiredMixin, ListView):
    template_name = 'search_results.html'
    context_object_name = 'notes'
    model = Note

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Note.objects.filter(Q(title__icontains=query) | Q(user__username__icontains=query))
class NotesListView(LoginRequiredMixin,ListView):
    template_name = 'notes.html'
    context_object_name = 'notes'
    model = Note
    login_url = 'account_login'

class NoteDetailView(LoginRequiredMixin, DetailView):
    template_name = 'note_detail.html'
    context_object_name = 'note'
    model = Note
    login_url = 'account_login'


class NoteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'note_form.html'
    model = Note
    fields = ['title', 'content']
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'note_update.html'
    model = Note
    fields = ['title', 'content']
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'note_delete.html'
    model = Note
    success_url = reverse_lazy('notes')
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'comment_form.html'
    model = Comment
    fields = ['content']
    login_url = 'account_login'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.note = Note.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['note'] = Note.objects.get(pk=self.kwargs['pk'])
        return context
    
    def get_success_url(self):
        return reverse_lazy('note-detail', kwargs={'pk': self.kwargs['pk']})
    

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'comment_form.html'
    model = Comment
    fields = ['content']
    login_url = 'account_login'

    def get_object(self, queryset=None):
        comment = Comment.objects.get(pk=self.kwargs['comment_pk'])
        return comment

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            raise PermissionDenied('You do not have permission to edit this comment.')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['note'] = Note.objects.get(pk=self.kwargs['pk'])
        context['comment'] = Comment.objects.get(pk=self.kwargs['comment_pk'])
        return context
    
    def get_success_url(self):
        return reverse_lazy('note-detail', kwargs={'pk': self.kwargs['pk']})
    

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'comment_delete.html'
    model = Comment
    success_url = reverse_lazy('notes')
    login_url = 'account_login'

    def get_object(self, queryset=None):
        comment = Comment.objects.get(pk=self.kwargs['comment_pk'])
        return comment

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            raise PermissionDenied('You do not have permission to delete this comment.')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['note'] = Note.objects.get(pk=self.kwargs['pk'])
        context['comment'] = Comment.objects.get(pk=self.kwargs['comment_pk'])
        return context
    
    def get_success_url(self):
        return reverse_lazy('note-detail', kwargs={'pk': self.kwargs['pk']})
    

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(user=self.request.user)
        return context