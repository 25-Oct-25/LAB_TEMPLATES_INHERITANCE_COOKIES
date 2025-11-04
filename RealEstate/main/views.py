from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
# Create your views here.
def home_view(request : HttpRequest):
    return render(request,"main/home.html")


def properties_view(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'main/properties.html', {"properties": properties})

def contact_view(request : HttpRequest):
    return render(request,"main/contact.html")

def about_view(request : HttpRequest):
    return render(request,"main/about.html")

def switch_mode(request):
    current_mode=request.COOKIES.get('theme','light')
    new_mode='dark' if current_mode == 'light' else 'light'

    response=redirect(request.META.get('HTTP_REFERER','/'))
    response.set_cookie('theme',new_mode,max_age=60*60*24*30)
    return response

def services_view(request : HttpRequest):
    return render(request,"main/services.html")

