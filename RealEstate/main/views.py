from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, cookie

# Create your views here.
def home_view(request: HttpRequest):
    return render(request, "main/index.html")

def properties_view(request: HttpRequest):
    properties = [
        {"id": 1, "title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"id": 2, "title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"id": 3, "title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"id": 4, "title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'main/properties.html', {"properties": properties})

def property_detail_view(request: HttpRequest, property_id: int):
    properties = [
        {"id": 1, "title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"id": 2, "title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"id": 3, "title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"id": 4, "title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    property = next((p for p in properties if p["id"] == property_id), None)
    return render(request, 'main/property_detail.html', {"property": property})

def about_view(request:HttpRequest):
    return render(request, "main/about_us.html")

def contact_us_view(request: HttpRequest):
    return render(request, "main/contact_us.html")

def set_theme(request, mode):
    response = redirect(request.GET.get('HTTP_REFERER', '/'))
    if mode in ['dark', 'light']:
        response.set_cookie('theme', mode, max_age=60*60*24) 
    return response