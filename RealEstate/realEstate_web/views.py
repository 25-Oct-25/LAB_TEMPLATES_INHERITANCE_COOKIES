from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

def home(request : HttpRequest):
    
    return render(request, "realEstate_web/home.html")


def properties(request : HttpRequest):
    
    return render(request, "realEstate_web/properties.html")


def contact(request : HttpRequest):
    
    return render(request, "realEstate_web/contact.html")

def dark_mode(request : HttpRequest):
    current = request.COOKIES.get('theme', 'light')
    mode='dark' if current == 'light' else 'light'
    response= redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie("theme", "dark", max_age=60*60)
    
    return response    
