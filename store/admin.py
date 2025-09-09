from django.contrib import admin
from .models import Category, Product, ProductImage, ProductAttribute, Wishlist

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductAttribute)
admin.site.register(Wishlist)

