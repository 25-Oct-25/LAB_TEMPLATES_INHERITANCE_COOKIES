from django.shortcuts import render, redirect
from django.urls import reverse

THEME_COOKIE = "UI_PALETTE_MODE"
THEME_MAX_AGE = 60 * 60 * 24 * 365  

def _theme_from_request(request):
    return request.COOKIES.get(THEME_COOKIE, "light")

def _render_with_theme(request, template_name, context=None):
    ctx = context or {}
    ctx["ui_mode"] = _theme_from_request(request) 
    return render(request, template_name, ctx)

def home_view(request):
    return _render_with_theme(request, "main/home.html")

def properties_view(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return _render_with_theme(request, "main/property_list.html", {"properties": properties})

def contact_view(request):
    return _render_with_theme(request, "main/contact.html")

def toggle_theme(request):
    set_to = request.GET.get("set_to") 
    current = _theme_from_request(request)

    if set_to in ["light", "dark"]:
       new_theme = set_to
    else:
       new_theme = "dark" if current != "dark" else "light"

    next_url = request.META.get("HTTP_REFERER") or reverse("main:home")
    resp = redirect(next_url)
    resp.set_cookie(THEME_COOKIE, new_theme, max_age=THEME_MAX_AGE, path="/")
    return resp
