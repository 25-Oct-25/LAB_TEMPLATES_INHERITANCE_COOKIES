from . import views
from django.urls import path 

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),  #خليت اول "" فاضي عشان يبدا لي من اول صفحه
    path("contact/", views.contact_view, name="contact_view"),
    path("properties/", views.properties, name="properties"),
    path("home/", views.home_view, name="home"),
    path("theme/<str:theme>/", views.set_theme_view, name="set_theme"),
] 