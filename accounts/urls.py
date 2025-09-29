from django.urls import path
from .views import CustomPasswordChangeView

urlpatterns = [
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
]