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
