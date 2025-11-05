from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def home_view(request:HttpRequest):

    return render(request, "main/index.html")


def properties_view(request: HttpRequest):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    
    return render(request, 'main/properties.html', {"properties": properties})

def services_view(request):
    return render(request, 'main/services.html')

def about_view(request):
    return render(request, 'main/about.html')

def contact_view(request):
    return render(request, 'main/contact.html')