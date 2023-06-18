from django.db import models

# Create your models here.
class Rates(models.Model):
    review_message = models.TextField()
    value=models.IntegerField()
    date = models.DateField()
    