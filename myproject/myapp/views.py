from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from .forms import UserRegistrationForm


def admin_view(request):
    return render(request, 'admins/index.html')


def frontend_view(request):
    return render(request, 'frontend/belle/index.html')



# def contact_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Save data to the database
#         Contact.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             subject=subject,
#             message=message
#         )

#         # Show a success message
#         messages.success(request, 'Your message has been sent successfully!')

#         # Redirect back to the contact form page
#         return redirect('contact_form')  # Correct: redirect to the URL pattern by name

#     # Render the contact form template
#     return render(request, 'myapp/contact-us.html')

# def index(request):
#     return render(request, 'myapp/index.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the user data to the database
#             return redirect('index')  # Redirect to the login page (adjust as needed)
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'myapp/register.html', {'form': form})

