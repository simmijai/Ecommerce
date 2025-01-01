from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    
    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Unique email
    phone = models.CharField(max_length=15, unique=True)  # Unique phone number
    password = models.CharField(max_length=255)  # Storing hashed password

    def save(self, *args, **kwargs):
        # Ensure password is hashed before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Clean method to validate unique email and phone
    def clean(self):
        if User.objects.filter(email=self.email).exists():
            raise ValidationError('Email already exists!')
        if User.objects.filter(phone=self.phone).exists():
            raise ValidationError('Phone number already exists!')
