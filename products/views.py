from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from basket.models import Basket, Favorite
from products.models import *


class ProductsView(ListView):
    model = Product
    template_name = 'products/shop-grid.html'
    context_object_name = 'products'
    paginate_by = 16

    def get_queryset(self):
        queryset = super().get_queryset()
        sub_category_id = self.kwargs.get('sub_category_id')
        return queryset.filter(sub_category_id=sub_category_id) if sub_category_id else queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.all()
        context['favorite'] = Favorite.objects.all()
        context['basket'] = Basket.objects.all()
        context['product_id'] = self.kwargs.get('product_id')
        return context


class AddToBasket(View, LoginRequiredMixin):

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        baskets = Basket.objects.filter(user=request.user, product=product)

        if not baskets.exists():
            Basket.objects.create(user=request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()

        return redirect('products:shop-grid')


class AddToFavorite(View, LoginRequiredMixin):

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        favorite = Favorite.objects.filter(user=request.user, product=product)

        if not favorite.exists():
            Favorite.objects.create(user=request.user, product=product)
        else:
            favorite.delete()

        return redirect('products:shop-grid')


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'products/category.html'
    context_object_name = 'categories'


class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'products/sub_shop.html'
    context_object_name = 'subcategories'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return SubCategory.objects.filter(category_id=category_id)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'products'

    def get_object(self, queryset=None):
        product_id = self.kwargs['product_id']
        return get_object_or_404(Product, id=product_id)


