from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from .forms import RegisterForm
from .models import CustomUser

# User Registration View
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Save but don’t commit
            user.is_candidate = True  # Set is_candidate
            user.save()  # Now save

            auth_login(request, user)  # Log user in
            messages.success(request, "Registration successful! Welcome to Interview Buddy 🎉")
            return redirect('dashboard')  
        else:
            print(form.errors)  # Debugging step to print form errors
            messages.error(request, "Registration failed. Please check the form and try again.")
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

# User Login View (Avoid overriding Django's login function)
def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)  # Authenticate user

        if user is not None:
            auth_login(request, user)  # Log in user
            messages.success(request, f"Welcome back, {user.username}! 🎉")
            return redirect("dashboard")  # Redirect to dashboard
        else:
            messages.error(request, "Invalid username or password. Please try again.")    
        
    return render(request, 'login.html')

# User Logout View (Avoid overriding Django's logout function)
def user_logout(request):
    auth_logout(request)
    return redirect('login')
