from django.shortcuts import render

# قائمة العقارات
PROPERTIES = [
    {"title": "Villa Modern in Malqa", "image": "images/villa1.jpg"},
    {"title": "Great Home for You in Rimal", "image": "images/villa2.jpg"},
    {"title": "Villa with 8 Bedrooms in Swedey", "image": "images/villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "images/villa4.jpg"},
]

# الصفحة الرئيسية
def home_view(request):
    return render(request, "core/home.html")

# صفحة العقارات
def properties_view(request):
    return render(request, "core/properties.html", {"properties": PROPERTIES})

# صفحة التواصل
def contact_view(request):
    return render(request, "core/contact.html")
