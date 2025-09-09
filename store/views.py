from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, SubCategory
from django import forms

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
            return redirect('subcategory_list')
    else:
        form = SubCategoryForm()
    return render(request, 'store/subcategory_form.html', {'form': form})

def subcategory_update(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    form = SubCategoryForm(request.POST or None, instance=subcategory)
    if form.is_valid():
        form.save()
        return redirect('subcategory_list')
    return render(request, 'store/subcategory_form.html', {'form': form})

def subcategory_delete(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    subcategory.delete()
    return redirect('subcategory_list')
