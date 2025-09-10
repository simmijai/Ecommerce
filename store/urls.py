from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name="category_list"),
    path('categories/add/', views.category_create, name="category_add"),
    path('categories/<int:pk>/edit/', views.category_create, name="category_edit"),
    path('categories/<int:pk>/delete/', views.category_delete, name="category_delete"),
    
    
   path('subcategories/', views.subcategory_list, name='subcategory_list'),
    path('subcategories/add/', views.subcategory_create, name='subcategory_add'),
    path('subcategories/edit/<int:pk>/', views.subcategory_update, name='subcategory_edit'),
    path('subcategories/delete/<int:pk>/', views.subcategory_delete, name='subcategory_delete'),
    


   path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('image/delete/<int:pk>/', views.image_delete, name='image_delete'),
]
