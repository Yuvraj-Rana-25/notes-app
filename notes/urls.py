from django.urls import path
from .views import HomePageView, NotesListView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('notes/', NotesListView.as_view(), name='notes'),
]