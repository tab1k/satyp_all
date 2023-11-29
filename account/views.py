from django.shortcuts import render
from django.views.generic import DetailView
from users.models import CustomUser


class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'account/user_profile.html'
    context_object_name = 'user'
