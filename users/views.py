from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixin
from .models import CustomUser, EmailVerification


class SignInView(LoginView):
    template_name = 'users/signin.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('main:index')


class SignUpView(SuccessMessageMixin,TitleMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:signin')
    success_message = 'Вы успешно зарегистрировались!'
    title = 'Регистрация'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        email = self.kwargs.get('email')
        code = self.kwargs.get('code')

        if email is not None and code is not None:
            try:
                user = CustomUser.objects.get(email=email)
                email_verification = EmailVerification.objects.filter(user=user, code=code)

                if email_verification.exists():
                    user.is_verified_email = True
                    user.save()
                    return super(EmailVerificationView, self).get(request, *args, **kwargs)
                else:
                    return render(request, 'main/index.html')
            except CustomUser.DoesNotExist:
                # Обработка случая, когда пользователя с указанным email не существует
                return render(request, 'main/index.html')
        else:
            # Обработка случая, когда email или code не были предоставлены
            return HttpRespconseBadRequest("Email и code должны быть предоставлены в URL.")

