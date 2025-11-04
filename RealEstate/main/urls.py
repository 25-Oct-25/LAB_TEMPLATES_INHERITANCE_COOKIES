from django.urls import path
from . import views
app_name = "main"
urlpatterns = [path('', views.home_view,name='home'),

               path('properties/', views.properties_view,name='properties'),
               path('contact/', views.contact_view,name='contact'),
               path('about/', views.about, name='about'),
               path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
               ]
