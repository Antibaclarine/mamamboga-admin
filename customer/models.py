from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=8)
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=10)
    contacts = models.CharField(max_length=20)
