# from django.urls import path
# from . import views

# urlpatterns = [
#     path('greet/', views.greet, name='greet'),
#     path('', views.landing_page_view, name='landingpage'),
#     path('pricing/', views.pricing_page_view, name='pricing'),
#     path('contact/', views.contact_page_view, name='contact'),
#     path('student/', views.StudentInfoView, name='student'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page_view, name='landing_page'),
    path('pricing/', views.pricing_page_view, name='pricing_page'),
    path('contact/', views.contact_page_view, name='contact_page'),
    path('student/', views.student_info_view, name='student_info'),
    path('greet/', views.greet, name='greet'),
]