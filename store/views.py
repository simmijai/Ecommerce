from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, SubCategory
from django import forms

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductImage, ProductAttribute
from .forms import ProductForm

# --------- FORMS ---------
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description']

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'name', 'slug', 'description']

# --------- CATEGORY CRUD ---------
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'store/category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'store/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')

# --------- SUBCATEGORY CRUD ---------
def subcategory_list(request):
    subcategories = SubCategory.objects.select_related('category').all()
    return render(request, 'store/subcategory_list.html', {'subcategories': subcategories})

def subcategory_create(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:subcategory_list')
    else:
        form = SubCategoryForm()
    return render(request, 'store/subcategory_form.html', {'form': form})

def subcategory_update(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    form = SubCategoryForm(request.POST or None, instance=subcategory)
    if form.is_valid():
        form.save()
        return redirect('store:subcategory_list')
    return render(request, 'store/subcategory_form.html', {'form': form})

def subcategory_delete(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    subcategory.delete()
    return redirect('store:subcategory_list')








from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductImage
from .forms import ProductForm

# Create product
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form})


# Update product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form})


# List products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')

# Delete single image
def image_delete(request, pk):
    image = get_object_or_404(ProductImage, pk=pk)
    product_id = image.product.id
    image.delete()
    return redirect('product_update', pk=product_id)



# def home(request):
#     products = Product.objects.all()  # sab products fetch
#     return render(request, "store/home.html", {"products": products})



from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Product

from django.core.paginator import Paginator

def home(request):
    products_list = Product.objects.all().order_by('id')  # order by id
    paginator = Paginator(products_list, 12)  # 12 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, "store/home.html", {"products": products})


# def home(request):
#     products = Product.objects.all()
#     return render(request, "store/home.html", {"products": products})

def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, "store/category_products.html", {"category": category, "products": products})

def subcategory_products(request, category_slug, subcategory_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug, category=category)
    products = Product.objects.filter(subcategory=subcategory)
    return render(request, "store/subcategory_products.html", {
        "category": category,
        "subcategory": subcategory,
        "products": products
    })



from .models import Product, ProductImage

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    images = ProductImage.objects.filter(product=product)

    context = {
        "product": product,
        "images": images,
    }
    return render(request, "store/product_detail.html", context)






from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductImage
from django.views.decorators.http import require_POST

# ---- helpers ----
def _get_cart(request):
    return request.session.get("cart", {})

def _save_cart(request, cart):
    request.session["cart"] = cart
    request.session.modified = True

# ---- add to cart ----
@require_POST
def add_to_cart(request, product_id):
    quantity = int(request.POST.get("quantity", 1))
    product = get_object_or_404(Product, id=product_id)

    cart = _get_cart(request)
    pid = str(product_id)

    if pid in cart:
        cart[pid]["quantity"] = cart[pid].get("quantity", 0) + quantity
    else:
        cart[pid] = {
            "name": product.name,
            "price": str(product.price),   # store as string to avoid JSON/Decimal issues
            "quantity": quantity,
            "image": product.images.first().image.url if product.images.exists() else None,
        }

    _save_cart(request, cart)
    return redirect("store:cart_detail")


# ---- cart detail ----
def cart_detail(request):
    cart = _get_cart(request)
    items = []
    total = Decimal("0.00")

    for pid, item in cart.items():
        price = Decimal(item["price"])
        qty = int(item["quantity"])
        subtotal = price * qty
        total += subtotal

        # try fresh product (optional)
        try:
            product = Product.objects.get(id=int(pid))
        except Product.DoesNotExist:
            product = None

        items.append({
            "product": product,
            "product_id": pid,
            "name": item["name"],
            "price": price,
            "quantity": qty,
            "image": item.get("image"),
            "subtotal": subtotal,
        })

    return render(request, "store/cart.html", {"items": items, "total": total})


# ---- update quantity (POST) ----
@require_POST
def update_cart(request, product_id):
    quantity = int(request.POST.get("quantity", 1))
    cart = _get_cart(request)
    pid = str(product_id)
    if pid in cart:
        if quantity > 0:
            cart[pid]["quantity"] = quantity
        else:
            del cart[pid]
        _save_cart(request, cart)
    return redirect("store:cart_detail")


# ---- remove item ----
@require_POST
def remove_from_cart(request, product_id):
    cart = _get_cart(request)
    pid = str(product_id)
    if pid in cart:
        del cart[pid]
        _save_cart(request, cart)
    return redirect("store:cart_detail")


# ---- simple checkout placeholder ----
def checkout(request):
    # Replace with real checkout later
    return render(request, "store/checkout.html")

