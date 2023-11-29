from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from products.models import *


class ProductsView(ListView):
    template_name = 'products/shop-grid.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        # Ваша логика фильтрации и сортировки продуктов
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавление категорий в контекст
        context['categories'] = ProductCategory.objects.all()
        return context