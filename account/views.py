from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView
from account.forms import UserProfileForm
from basket.models import Favorite, Basket
from users.models import CustomUser


class UserProfileView(UpdateView, LoginRequiredMixin):
    model = CustomUser
    form_class = UserProfileForm
    template_name = 'account/user_profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:account:profile', args=[self.request.user.pk])


class UserOrdersView(ListView):
    model = CustomUser
    template_name = 'account/user_orders.html'
    context_object_name = 'user'


class UserAddressView(View):

    def get(self, request):
        return render(request, 'account/user_address.html')


class UserPaymentView(View):

    def get(self, request):
        return render(request, 'account/user_payment.html')


class UserNotificationView(View):

    def get(self, request):
        return render(request, 'account/user_notificationsettings.html')


class WishlistView(LoginRequiredMixin, View):
    template_name = 'account/user_wishlist.html'

    def get(self, request, *args, **kwargs):
        # Получаем избранные объекты для текущего пользователя
        favorites = Favorite.objects.filter(user=request.user)

        # Передаем избранные объекты в шаблон
        context = {'favorites': favorites}
        return render(request, self.template_name, context)


class UserCartView(LoginRequiredMixin, View):

    template_name = 'account/user_cart.html'

    def get(self, request):

        basket = Basket.objects.filter(user=request.user).order_by('-created_timestamp')

        context = {
            'basket' : basket,
        }

        return render(request, self.template_name, context)
