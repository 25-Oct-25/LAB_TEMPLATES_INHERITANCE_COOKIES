from django.shortcuts import render, redirect
from django.http import HttpRequest

def home_view(request: HttpRequest):
    return render(request, 'main/home.html')


def properties_view(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'main/properties.html', {"properties": properties})


def contact_view(request: HttpRequest):
    return render(request, "main/contact.html")


# 🌓 هذا هو الفيو المسؤول عن تبديل الوضع الداكن والفاتح
def set_theme(request, theme):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    if theme in ['light', 'dark']:
        response.set_cookie('theme', theme, max_age=60*60*24*30)  # يخزّن التفضيل لمدة شهر
    return response
