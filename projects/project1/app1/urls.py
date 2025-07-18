from django.urls import path,include
from . import views

urlpatterns = [
    path('landingPage',views.landingPageView,name='landingPage'),
]
