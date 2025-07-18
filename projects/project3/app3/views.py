# from django.urls import path
# from . import views

# urlpatterns = [
#     path('greet/', views.greet, name='greet'),
#     path('', views.landing_page_view, name='landingpage'),
#     path('pricing/', views.pricing_page_view, name='pricing'),
#     path('contact/', views.contact_page_view, name='contact'),
#     path('student/', views.StudentInfoView, name='student'),
# ]

from django.shortcuts import render
from .forms import StudentForm, ContactForm
from django.http import HttpResponse

# def greet(request):
#     return HttpResponse("Hello from greet view!")

users = [
    {'name': 'Amogh', 'age': 21},
    {'name': 'Brahma', 'age': 21},
    {'name': 'Joe Goldberg', 'age': 21},
]

cards = [
    {'title': 'Personal', 'description': 'This is a personal plan', 'original_price': 100, 'updated_price': 110},
    {'title': 'Starter', 'description': 'This is a Starter plan', 'original_price': 100, 'updated_price': 50},
    {'title': 'Advanced', 'description': 'This is an Advanced plan', 'original_price': 100, 'updated_price': 1110},
]


def student(request):
    form = StudentForm()
    return render(request, 'student.html', {'form': form})

def landing(request):
    return render(request, 'landing.html')


def pricing(request):
    return render(request, 'pricing.html', {'cards': cards})


def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            print("Your request is recorded")
        else:
            print("Your request is not recorded")
        return render(request, 'contact.html', {'form': f})
    else:
        f = ContactForm()
        return render(request, 'contact.html', {'form': f})