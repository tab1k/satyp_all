from django.views.generic import TemplateView
from basket.models import Favorite, Basket
from products.models import *


class IndexView(TemplateView):

    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.all()
        context['category'] = ProductCategory.objects.all()
        context['favorite'] = Favorite.objects.all()
        context['basket'] = Basket.objects.all()

