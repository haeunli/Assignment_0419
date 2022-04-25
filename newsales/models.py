from django.db import models

from django.utils import timezone

class Sales(models.Model):
    continents = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    categories = models.CharField(max_length=50)
    sales = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    order_priority = models.CharField(max_length=10)
