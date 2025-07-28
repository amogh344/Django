from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import StudentForm, ContactForm, RegisterForm, LoginForm

# Sample user and card data
users = [
    {'name': 'Amogh', 'age': 21},
    {'name': 'Brahma', 'age': 21},
    {'name': 'Joe Goldberg', 'age': 21},
]

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

# View to handle login
def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Replace with actual home page name
    return render(request, 'login.html', {'form': form})

# View to handle student form
def student(request):
    form = StudentForm()
    return render(request, 'student.html', {'form': form})

# Landing page view
def landing(request):
    return render(request, 'landing.html')

# Pricing page with card info
def pricing(request):
    return render(request, 'pricing.html', {'cards': cards})

# User registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace with actual login page URL name
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Contact form view
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Your request is recorded")
        else:
            print("Your request is not recorded")
        return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})