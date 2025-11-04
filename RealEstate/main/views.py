from django.shortcuts import render, redirect

PROPERTIES = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
]


def _is_dark(request):
    
    return request.COOKIES.get('dark_mode', 'false') == 'true'


def home(request):

    context = {"properties": PROPERTIES[:3], "dark_mode": _is_dark(request)}
    return render(request, "main/home.html", context)


def properties(request):

    context = {"properties": PROPERTIES, "dark_mode": _is_dark(request)}
    return render(request, "main/properties.html", context)

def view_details(request):

    context = {"properties": PROPERTIES, "dark_mode": _is_dark(request)}
    return render(request, "main/details.html", context)


def contact(request):

    return render(request, "main/contact.html", {"dark_mode": _is_dark(request)})


def toggle_dark_mode(request):

    redirect_to = request.META.get("HTTP_REFERER") or "/"
    response = redirect(redirect_to)

    current = request.COOKIES.get("dark_mode", "false")
    new_value = "false" if current == "true" else "true"

    response.set_cookie("dark_mode", new_value, max_age=60 * 60 * 24 * 30)
    return response
