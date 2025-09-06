from django.contrib import admin
from .models import Payment,Order,OrderItem
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)

