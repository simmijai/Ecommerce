from django.db import models
from accounts.models import User, Address
from store.models import Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    PAYMENT_METHODS = (
        ('cod', 'Cash on Delivery'),
        ('card', 'Card'),
        ('paypal', 'PayPal'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    placed_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def subtotal(self):
        return self.price * self.quantity

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_id = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    paid_at = models.DateTimeField(auto_now_add=True)
