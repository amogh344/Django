from django.urls import path
from . import views

urlpatterns = [
    path('greet/', views.greet, name='greet'),
    path('', views.landing_page_view, name='landingpage'),
    path('pricing/', views.pricing_page_view, name='pricing'),
    path('contact/', views.contact_page_view, name='contact'),
    path('student/', views.StudentInfoView, name='student'),
]