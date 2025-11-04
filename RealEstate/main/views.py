from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home_view(request:HttpRequest):
    return render(request,"main/home.html")

def properties_view(request:HttpRequest):
    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
    return render(request,"main/properties.html",context={"prop":properties})

def contact_view(request:HttpRequest):
    return render(request,"main/contact.html")

def mode_view(request:HttpRequest,mode):
    res=redirect(request.GET.get("next","/"))# "/": for defult query
    if mode=="light":
        res.set_cookie("mode","light")
    elif mode=="dark":
        res.set_cookie("mode","dark")
    return res

def info_properties_view(request:HttpRequest,title,image):
    context = {
        'title': title,
        'image': image,
    }
    return render(request,"main/info_prop.html",context)