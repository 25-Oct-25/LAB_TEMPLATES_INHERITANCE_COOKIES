from django.shortcuts import render
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