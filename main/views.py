from django.shortcuts import render
from django.views import View

from basket.models import Favorite, Basket
from products.models import *


class IndexView(View):

    def get(self, request):
        product = Product.objects.all()
        category = ProductCategory.objects.all()
        favorite = Favorite.objects.all()
        basket = Basket.objects.all()

        context = {
            'product' : product,
            'category' : category,
            'favorite' : favorite,
            'basket' : basket,
        }

        return render(request, 'main/index.html', context)