from django.urls import path
from . import views
app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("properties/", views.properties, name="properties"),
    path("contact/", views.contact, name="contact"),
    path('dark_mode/', views.dark_mode, name='dark_mode'),
]