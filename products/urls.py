from products.views import *
from django.urls import path, include

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='shop-grid'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('subcategories/<int:category_id>/', SubCategoryListView.as_view(), name='subcategories'),
    path('products/<int:sub_category_id>/', ProductsView.as_view(), name='products'),
    path('add-to-basket/<int:product_id>/', AddToBasket.as_view(), name='add-to-basket'),
    path('add-to-favorite/<int:product_id>/', AddToFavorite.as_view(), name='add-to-favorite'),
]
