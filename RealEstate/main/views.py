from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def base_view(request):


    return render(request, "main/base.html", )

def home_view(request):

    cookie_value = request.COOKIES.get('background', "white")


    response = render(request, "main/home.html", {"background": cookie_value})
    return response

def contact_view(request):

    return render(request, "main/contact.html", )


def properties_view(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great Home for You in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 Bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    context = {
        'properties': properties 
    }
    return render(request, 'main/properties.html', context)

def dark_mode(request: HttpRequest, mode: str):
    if mode not in ['light', 'dark']:
        mode = 'light'
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('mode', mode, max_age=60*60*24*30)
    return response