from django.contrib.auth.views import LogoutView

from account.views import *
from django.urls import path

app_name = 'account'

urlpatterns = [
    path("profile/<int:pk>/", UserProfileView.as_view(), name='profile'),
    path("orders/", UserOrdersView.as_view(), name='orders'),
    path("address/", UserAddressView.as_view(), name='address'),
    path("payment/", UserPaymentView.as_view(), name='payment'),
    path("notification/", UserNotificationView.as_view(), name='notification'),
    path("wishlist/", WishlistView.as_view(), name='wishlist'),
    path("cart/", UserCartView.as_view(), name='cart'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
