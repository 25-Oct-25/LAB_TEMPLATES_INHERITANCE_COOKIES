from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

PROPERTIES = [

    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},

]

def _theme_from_request(request):
    return request.COOKIES.get("theme", "light")

def index(request):
    theme = _theme_from_request(request)
    return render(request, "main/index.html", {"theme": theme, "properties": PROPERTIES[:4]})

def properties_page(request):
    theme = _theme_from_request(request)
    return render(request, "main/properties.html", {"theme": theme, "properties": PROPERTIES})

def contact(request):
    theme = _theme_from_request(request)
    return render(request, "main/contact.html", {"theme": theme})

def toggle_theme(request):
    current = request.COOKIES.get("theme", "light")
    new_theme = "dark" if current != "dark" else "light"
    resp = HttpResponseRedirect(reverse("index"))
    resp.set_cookie("theme", new_theme, max_age=60*60*24*90, httponly=False, samesite="Lax")
    return resp
def index(request):
    theme = _theme_from_request(request)
    return render(
        request,
        "main/index.html",
        {"theme": theme, "properties": PROPERTIES[:3], "page": "home"},  # ← أضف page
    )

def index(request):
    theme = _theme_from_request(request)
    return render(
        request,
        "main/index.html",
        {"theme": theme, "properties": PROPERTIES[:3], "page": "home"},
    )