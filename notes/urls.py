from django.urls import path
from .views import HomePageView, NotesListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, SearchResultsListView, UserProfileView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('notes/', NotesListView.as_view(), name='notes'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile'),
    path('notes/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('notes/new/', NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('notes/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('notes/<int:pk>/comment/<int:comment_pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('notes/<int:pk>/comment/<int:comment_pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('search/', SearchResultsListView.as_view(), name='search-results'),
]