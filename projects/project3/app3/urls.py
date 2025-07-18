from django.urls import path
from . import views

urlpatterns = [
    # path('greet/', views.greet, name='greet'),
    path('', views.landing, name='landing'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('student/', views.student, name='student'),
]