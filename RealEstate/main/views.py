from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_view(request:HttpRequest):
    
    return render(request, "main/home.html")

def properties_view(request:HttpRequest):

    properties = [

        {"title" : "Villa Modern in Malqa", "image" : "/static/images/villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "/static/images/villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "/static/images/villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "/static/images/villa4.jpg"},
    ]

    return render(request, "main/properties.html", context= {"properties_list": properties})

def contact_view(request:HttpRequest):

    return render(request, "main/contact.html")

#light-dark mood cookies

def set_theme_view(request: HttpRequest, theme : str):
    response = redirect(request.META.get('HTTP_REFERER','/'))
    if theme in ['light', 'dark']:
        response.set_cookie('theme', theme, max_age=365*24*60*60)
    return response