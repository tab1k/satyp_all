from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin


class SignInView(LoginView):
    template_name = 'users/signin.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('main:index')


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:signin')
    success_message = 'Вы успешно зарегистрировались!'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)