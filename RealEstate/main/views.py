from django.shortcuts import render, redirect
from django.urls import reverse

THEME_KEY = "UI_THEME_MODE" 
THEME_MAX_AGE = 60 * 60 * 24 * 365 

def get_theme(request):
    return request.COOKIES.get(THEME_KEY, "light")

def render_theming(request, template_name, ctx=None):
    context = ctx or {}
    context["theme_mode"] = get_theme(request) 
    return render(request, template_name, context)

def home_view(request):
    return render_theming(request, "main/home.html")

def properties_view(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render_theming(request, "main/properties.html", {"properties": properties})

def contact_view(request):
    return render_theming(request, "main/contact.html")

def switch_theme(request):
    set_to = request.GET.get("set")
    current = get_theme(request)

    if set_to in ("light", "dark"):
        new_theme = set_to
    else:
        new_theme = "dark" if current != "dark" else "light"

    next_url = request.META.get("HTTP_REFERER") or reverse("main:home")
    resp = redirect(next_url)
    resp.set_cookie(THEME_KEY, new_theme, max_age=THEME_MAX_AGE, path="/")
    return resp
