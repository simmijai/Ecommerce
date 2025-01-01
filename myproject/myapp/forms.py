from django import forms
from .models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']

    # Clean email to ensure it is unique
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already in use!")
        return email

    # Clean phone number to ensure it is unique
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if User.objects.filter(phone=phone).exists():
            raise ValidationError("Phone number is already in use!")
        return phone
