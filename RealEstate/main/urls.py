from . import views
from django.urls import path

app_name = "main"
urlpatterns = [

    path("", views.home_view,name="home_view"),
    path("prop/", views.properties_list,name="properties_list"),
    path("cont/", views.contact,name="contact"),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),    

]
