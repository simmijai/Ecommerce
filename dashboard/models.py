from django.db import models
from store.models import Product
from orders.models import Order

class SalesReport(models.Model):
    date = models.DateField()
    total_orders = models.PositiveIntegerField()
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2)
    total_products_sold = models.PositiveIntegerField()

class ProductReport(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sold_quantity = models.PositiveIntegerField()
    revenue_generated = models.DecimalField(max_digits=12, decimal_places=2)
