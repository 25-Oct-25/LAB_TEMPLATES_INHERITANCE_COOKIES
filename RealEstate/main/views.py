from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def home_view(request : HttpRequest):
    theme = request.COOKIES.get('theme', 'light')  
    context = {'theme': theme} 
    return render(request, 'main/home.html', context)

def properties_view(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'main/properties.html', {"properties": properties, "theme": theme})


def contact_view(request : HttpRequest):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'main/contact.html', {"theme": theme})
def about(request):
    return render(request, 'main/about.html')

def toggle_theme(request):
    current_theme = request.COOKIES.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('theme', new_theme, max_age=60*60*24*30)
    
    return response
