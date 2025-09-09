from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address, OTP, Notification

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('role','phone','email_verified')}),
    )
    list_display = ('username','email','role','is_active','is_staff')

admin.site.register(Address)
admin.site.register(OTP)
admin.site.register(Notification)
