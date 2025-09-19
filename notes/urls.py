from django.urls import path
from .views import HomePageView, NotesListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('notes/', NotesListView.as_view(), name='notes'),
    path('notes/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('notes/new/', NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]