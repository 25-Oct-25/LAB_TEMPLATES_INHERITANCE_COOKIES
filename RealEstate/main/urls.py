from django.urls import path
from . import views



app_name = "main"
urlpatterns = [
    path('',views.home_view,name="home_view"),
    path('properties/',views.properties_view,name="properties_view"),
    path('contact/',views.contact_view,name="contact_view"),
    path('about/',views.about_view,name="about_view"),
    path('switch_mode/',views.switch_mode,name="switch_mode"),
    path('services/',views.services_view,name="services_view"),


]