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
