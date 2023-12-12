from django.views.generic import TemplateView, ListView
from basket.models import Favorite, Basket
from products.models import *
from common.views import TitleMixin


class IndexView(TitleMixin, ListView):
    model = Product
    template_name = 'main/index.html'
    title = 'Главная'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.all()
        context['favorite'] = Favorite.objects.all()
        context['basket'] = Basket.objects.all()
        return context


class ShopListView(ListView):
    model = Shop
    template_name = 'shop/shops.html'

