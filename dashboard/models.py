from django.db import models


class Order(models.Model):
    product_category = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=30)
    unit_price = models.IntegerField()

