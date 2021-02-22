from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

# class ProfileView(DetailView):
#     model = User
#     template_name = 'profile.html'

#     def get_object(self):
#         return get_object_or_404(User, username=self.kwargs['username'])
