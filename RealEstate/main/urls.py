from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("properties/", views.properties, name="properties"),
    path("contact/", views.contact, name="contact"),
    path("view/details/", views.view_details , name="view_details"),
    path("toggle-dark-mode/", views.toggle_dark_mode, name="toggle_dark_mode"),
]
