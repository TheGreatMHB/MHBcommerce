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
    context = {

    }
    return render(request, "contact.html", context)
