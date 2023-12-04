from products.views import *
from django.urls import path, include

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='shop-grid'),
    path('products/<int:sub_category_id>/', ProductsView.as_view(), name='products_by_subcategory'),
    path('categories', CategoryListView.as_view(), name='category'),
    path('categories/<int:category_id>', SubCategoryListView.as_view(), name='sub_category'),
    path('add-to-basket/<int:product_id>/', AddToBasket.as_view(), name='add-to-basket'),
    path('add-to-favorite/<int:product_id>/', AddToFavorite.as_view(), name='add-to-favorite'),
    path('product/<int:product_id>', ProductDetailView.as_view(), name='product'),
]
