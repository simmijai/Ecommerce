from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if not user.is_active:
                messages.error(request, "Your account is disabled. Please contact support.")
                return redirect("accounts:login")

            login(request, user)

            # ✅ Role-based redirection
            if user.role in ["admin", "staff"]:
                return redirect("dashboard:index")     # admin & staff → dashboard
            elif user.role == "customer":
                return redirect("store:home")  # customer → product list
            else:
                messages.error(request, "Role not recognized.")
                logout(request)
                return redirect("accounts:login")

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")
# # Login view
# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
            
#             # Role-based redirection
#             if user.role in ["admin", "staff"]:
#                 return redirect("dashboard:index")  # admin & staff → dashboard
#             # elif user.role == "customer":
#             #     return redirect("store:home")      # customer → store
#             else:
#                 messages.error(request, "Invalid role.")
#         else:
#             messages.error(request, "Invalid username or password.")
    
#     return render(request, "accounts/login.html")

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect("accounts:login")


# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

# --------------------
# Register User
# --------------------
def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "customer"   # default role
            user.save()

            messages.success(request, "Account created successfully! Please log in.")
            return redirect("accounts:login")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})

