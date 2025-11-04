from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("properties/", views.properties_page, name="properties"),
    path("contact/", views.contact, name="contact"),
    path("toggle-theme/", views.toggle_theme, name="toggle_theme"),
]
