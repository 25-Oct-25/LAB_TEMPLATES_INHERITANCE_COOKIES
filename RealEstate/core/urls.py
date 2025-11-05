from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    
    path('properties/', views.properties_view, name='properties'),
    
    path('contact/', views.contact_view, name='contact'),
]