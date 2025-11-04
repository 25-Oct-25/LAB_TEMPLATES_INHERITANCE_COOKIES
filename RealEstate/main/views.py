from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_view(request : HttpRequest): 
    return render(request, "main/index.html")# اعطيه باث ال templates

def contact_view(request : HttpRequest): 
    return render(request, "main/contact.html")

def properties(request : HttpRequest): 
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedy", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'main/properties.html', {'properties': properties })

def set_theme_view(request : HttpRequest, theme : str):
    """View to set theme cookie and redirect back"""
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    if theme in ['light', 'dark']:
        response.set_cookie('theme', theme, max_age=365*24*60*60)  # 1 year
    return response
