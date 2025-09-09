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
]
