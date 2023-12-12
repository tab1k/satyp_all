from django.http import Http404
from django.views.generic import ListView, DetailView
from shop.models import *


class ShopsListView(ListView):
    model = Shop
    template_name = 'shop/shops.html'
    context_object_name = 'shops'
    paginate_by = 16


class ShopsDetailView(DetailView):
    model = Shop
    template_name = 'shop/shops_single.html'
    context_object_name = 'detail'

    def get_object(self, queryset=None):
        shop_id = self.kwargs.get('shop_id')
        queryset = Shop.objects.filter(pk=shop_id)

        try:
            obj = queryset.get()
        except Shop.DoesNotExist:
            raise Http404("Shop does not exist")

        return obj


