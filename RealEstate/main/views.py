from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

PROPERTIES = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
]

def home_view(request: HttpRequest):
    theme = request.COOKIES.get('theme', 'light') 
    return render(request, 'main/index.html', context={'properties': PROPERTIES, 'theme': theme})

def properties_view(request: HttpRequest):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'main/properties.html', context={'properties': PROPERTIES, 'theme': theme})

def contact_view(request: HttpRequest):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'main/contact.html', context={'properties': PROPERTIES, 'theme': theme})

def set_theme(request: HttpRequest, mode: str):
    response = redirect(request.META.get('HTTP_REFERER', '/')) 
    if mode in ['light', 'dark']:
        response.set_cookie('theme', mode, max_age=60*60*24*365) 
    return response
