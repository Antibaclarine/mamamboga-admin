from django.db import models

# Create your models here.
class Add(models.Model):
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.PositiveIntegerField()
    shippingcost = models.DecimalField(max_digits=6,decimal_places=2)
    paymentoptions = models.CharField(max_length=15)
    