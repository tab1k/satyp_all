from django.shortcuts import render
from django.views import View
from products.models import *


class IndexView(View):

    def get(self, request):
        product = Product.objects.all()
        category = ProductCategory.objects.all()

        context = {
            'product' : product,
            'category' : category,
        }

        return render(request, 'main/index.html', context)