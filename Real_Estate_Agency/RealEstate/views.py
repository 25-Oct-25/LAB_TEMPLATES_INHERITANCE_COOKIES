from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request : HttpRequest):
    content = "home"
    return HttpResponse(content)

def properties_view(request : HttpRequest):
    content = "properties"
    return HttpResponse(content)

def contact_view(request : HttpRequest):
    content = "contact"
    return HttpResponse(content)
