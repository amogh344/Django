from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TaskView

router = DefaultRouter()
router.register('tasks',TaskView)



urlpatterns = [
    path('', views.landing, name='landing'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('student/', views.student, name='student'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('api/',include(router.urls)),
]