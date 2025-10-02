from django.urls import path
from .views import NotesAPIView, NoteDetailAPIView, CommentAPIView, CommentDetailAPIView, NoteCommentAPIView


urlpatterns = [
    path("notes/<int:note_id>/comment/", NoteCommentAPIView.as_view(), name="note-comment"),
    path("comments/<int:pk>", CommentDetailAPIView.as_view(), name="comment-detail"),
    path("comments/", CommentAPIView.as_view(), name="comment-list"),
    path("<int:pk>", NoteDetailAPIView.as_view(), name="api-note-detail"),
    path("notes/", NotesAPIView.as_view(), name="notes-list"),
]