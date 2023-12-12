from django.urls import path, include
from shop.views import *

app_name = 'shop'

urlpatterns = [
    path('view/', ShopsListView.as_view(), name='shops'),
    path('view/<int:shop_id>/detail/', ShopsDetailView.as_view(), name='detail'),
]

