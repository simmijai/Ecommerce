from django.db import models
from django.contrib.auth.models import AbstractUser

# If you want to extend default Django User
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    # AbstractUser already has: username, email, password, is_active, first_name, last_name

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.address_line1}"
