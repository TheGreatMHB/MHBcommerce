from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    context = {

    }
    return render(request, "homePage.html", context)


def aboutus_page(request):
    context = {

    }
    return render(request, "about.html", context)


def contact_page(request):

    if request.method == "POST":
        print(request.method)
        print(request.POST)
        print(request.POST.get('Email'))
    context = {
        'title': "Contact Us",
        'subtitle': "Keep in touch with us",
    }
    return render(request, "Contact/view.html", context)
