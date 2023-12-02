from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from basket.models import Basket, Favorite
from products.models import *


class ProductsView(ListView):
    template_name = 'products/shop-grid.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавление категорий в контекст
        context['category'] = ProductCategory.objects.all()
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

        context = {
            'basket': Basket.objects.filter(user=request.user)
        }

        return render(request, 'products/shop-grid.html', context)


class AddToFavorite(View, LoginRequiredMixin):

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        favorite = Favorite.objects.filter(user=request.user, product=product)

        if not favorite.exists():
            Favorite.objects.create(user=request.user, product=product)
        else:
            favorite.delete()

        return redirect('products:shop-grid')

