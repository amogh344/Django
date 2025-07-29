from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, ContactForm, RegisterForm, LoginForm
from .models import Student, TaskBoard
from rest_framework import viewsets
from .serializers import TaskSerializer

# Pricing card data
cards = [
    {
        'title': 'Personal',
        'description': 'This is a personal plan',
        'original_price': 100,
        'updated_price': 110
    },
    {
        'title': 'Starter',
        'description': 'This is a Starter plan',
        'original_price': 100,
        'updated_price': 50
    },
    {
        'title': 'Advanced',
        'description': 'This is an Advanced plan',
        'original_price': 100,
        'updated_price': 1110
    },
]

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome , {username}!")
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('login')

    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('landing')

def student(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Student registered successfully.")
        return redirect('student')
    return render(request, 'student.html', {'form': form})

def landing(request):
    return render(request, 'landing.html')

def pricing(request):
    return render(request, 'pricing.html', {'cards': cards})

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')
    return render(request, 'register.html', {'form': form})

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        messages.success(request, "Your request has been recorded.")
        return redirect('contact')
    return render(request, 'contact.html', {'form': form})


class TaskView(viewsets.ModelViewSet):
    queryset = TaskBoard.objects.all()
    serializer_class = TaskSerializer