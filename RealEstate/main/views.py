from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, cookie

# Create your views here.
def home_view(request: HttpRequest):
    return HttpResponse(request, "main/index.html")

def properties_view(request: HttpRequest):
    return HttpResponse(request, "main/properties.html")

def contact_us_view(request: HttpRequest):
    return HttpResponse(request, "main/contact_us.html")