from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
# Create your views here.

def home(request:HttpRequest) -> HttpResponse:
    current_mode = request.COOKIES.get('mode','light')

    context ={
        'current_mode': current_mode
    }
    return render(request, 'main/home.html',context)


def set_theme(request, mode_name):
    if mode_name not in ['light', 'dark']:
        new_mode = 'light'
    else:
        new_mode = mode_name
        

    response = redirect(request.META.get('HTTP_REFERER', 'main:home'))
    

    response.set_cookie(
        'mode',
        new_mode,
        max_age=365*24*60*60
    )
    
    return response


def properties(request:HttpRequest) -> HttpResponse:
    current_mode = request.COOKIES.get('mode','light')
    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
    context ={
        'current_mode': current_mode,
        'properties': properties,
    }
    return render(request, 'main/properties.html', context)

def contact (request:HttpRequest) -> HttpResponse:
    current_mode = request.COOKIES.get('mode','light')

    context ={
        'current_mode': current_mode
    }
    return render(request, 'main/contact.html',context)