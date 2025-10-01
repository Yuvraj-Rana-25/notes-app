from django.urls import path
from .views import NotesAPIView


urlpatterns = [
    path("", NotesAPIView.as_view(), name="notes-list"),
]