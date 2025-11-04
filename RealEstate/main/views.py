from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# الصفحة الرئيسية
def home_view(request: HttpRequest):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, "main/index.html", {"theme": theme})

# صفحة العقارات
def properties_list(request: HttpRequest):
    theme = request.COOKIES.get('theme', 'light')

    properties = [
        {"title": "Villa Modern in Malqa", "image": "image/villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "image/villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "image/villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "image/villa4.jpg"},
    ]
    return render(request, "main/prop.html", {"properties": properties, "theme": theme})

# صفحة التواصل
def contact(request: HttpRequest):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, "main/cont.html", {"theme": theme})


def toggle_theme(request: HttpRequest):
    current_theme = request.COOKIES.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('theme', new_theme, max_age=60*60*24*365)  # سنة كاملة
    return response