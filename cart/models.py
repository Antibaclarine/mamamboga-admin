from django.db import models
from basket.models import Basket

class Cart(models.Model):
    products = models.ManyToManyField(Basket)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    shippingcost = models.DecimalField(max_digits=6, decimal_places=2)
    paymentoptions = models.CharField(max_length=15)

    def __str__(self):
        return f"Cart {self.pk}"