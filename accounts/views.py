from django.shortcuts import render
from allauth.account.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Password successfully changed.')
        return super().form_valid(form)