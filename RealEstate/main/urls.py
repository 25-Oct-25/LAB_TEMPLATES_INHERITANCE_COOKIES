from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("properties/", views.properties_view, name="properties_view"),
    path('properties/<int:property_id>/', views.property_detail_view, name='property_detail_view'),
    path('about/us/', views.about_view, name="about_view"),
    path("contact/us/", views.contact_us_view, name="contact_us_view"),
    path('set_theme/<str:mode>/', views.set_theme, name='set_theme'),
]