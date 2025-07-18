from django.shortcuts import render
from .forms import StudentForm, ContactForm
from django.http import HttpResponse

def greet(request):
    return HttpResponse("Hello from greet view!")

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

def landing_page_view(request):
    return render(request, 'landing_page.html')  # ✅ matches your template

def pricing_page_view(request):
    return render(request, 'pricing_page.html', {'cards': cards})  # ✅ matches your template

def contact_page_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Your request is recorded")
        else:
            print("Your request is not recorded")
        return render(request, 'contact_page.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact_page.html', {'form': form})

def student_info_view(request):
    form = StudentForm()
    return render(request, 'student_info.html', {'form': form})  # ✅ matches your file