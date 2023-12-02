from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from users.models import CustomUser


class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'account/user_profile.html'
    context_object_name = 'user'


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