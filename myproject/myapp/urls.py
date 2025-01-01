from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontend_view, name='frontend_home'),  # Default frontend
    path('admins/', views.admin_view, name='admin_home'),

]
