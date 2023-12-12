from django.db import models

RAITING_CHOICES = (
    ('1', '1 звезда'),
    ('2', '2 звезда'),
    ('3', '3 звезда'),
    ('4', '4 звезда'),
    ('5', '5 звезда'),
)


class Shop(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shops_images/', blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    delivery = models.BooleanField(default=False)
    pickup_available = models.BooleanField(default=True)
    raiting = models.CharField(choices=RAITING_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'