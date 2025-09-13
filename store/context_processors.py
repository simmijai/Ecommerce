from .models import Category

def categories_processor(request):
    categories = Category.objects.prefetch_related('subcategories').all()
    return {"categories": categories}

def cart_item_count(request):
    cart = request.session.get("cart", {})
    total_items = sum(item.get("quantity", 0) for item in cart.values())
    return {"cart_item_count": total_items}