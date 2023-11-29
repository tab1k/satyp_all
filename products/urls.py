from products.views import *
from django.urls import path, include

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='shop-grid'),
]
