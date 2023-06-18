from django.db import models

# Create your models here.
class Order(models.Model):
    quantity = models.IntegerField()
    date = models.DateTimeField()
    total = models.DecimalField(max_digits=10,decimal_places=2)
    name = models.CharField(max_length=20)