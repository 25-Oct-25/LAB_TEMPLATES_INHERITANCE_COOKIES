from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('set-theme/<str:mode_name>/', views.set_theme, name='set_theme')

]