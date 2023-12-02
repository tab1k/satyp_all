from django.db import models
from products.models import Product
from users.models import CustomUser


class Basket(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'В корзине пользователя {self.user} -> {self.product} ({self.quantity} шт.)'

    class Meta:
        verbose_name = 'Корзина пользователей'
        verbose_name_plural = 'Корзины пользователей'


class Favorite(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пользователю {self.user} понравился -> {self.product}.'

    class Meta:
        verbose_name = 'Понравившиеся пользователю'
        verbose_name_plural = 'Понравившиеся пользователям'
