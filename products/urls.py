from products.views import *
from django.urls import path, include

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='shop-grid'),
    path('add-to-basket/<int:product_id>/', AddToBasket.as_view(), name='add-to-basket'),
    path('add-to-favorite/<int:product_id>/', AddToFavorite.as_view(), name='add-to-favorite'),
]
