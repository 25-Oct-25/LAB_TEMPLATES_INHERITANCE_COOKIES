from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 
from django.shortcuts import resolve_url
from django.shortcuts import redirect

# Create your views here.

def home_view(request:HttpRequest):

    return render(request, "main/home.html")

def properties_view(request:HttpRequest):
        properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
        return render(request, "main/properties.html", {"properties": properties})

def contact_view(request:HttpRequest):

    return render(request, "main/contact.html")


def toggle_font(request):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    current_size = request.COOKIES.get('font_size', 'normal')


    if current_size == 'normal':
        response.set_cookie('font_size', 'large')
    else:
        response.set_cookie('font_size', 'normal')

    return response


