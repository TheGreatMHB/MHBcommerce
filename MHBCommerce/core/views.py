from django.shortcuts import render, redirect
from django.http import HttpResponse
from MHBCommerce.forms import ContactForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home_page(request):
    context = {

    }
    return render(request, "homePage.html", context)


def aboutus_page(request):
    context = {

    }
    return render(request, "about.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        if request.method == "POST":
            print(request.method)
            print(request.POST)
            print(request.POST.get('Email'))
    context = {
        'title': "Contact Us",
        'subtitle': "Keep in touch with us",
        'form': contact_form
    }
    return render(request, "Contact/view.html", context)


def register_page(request):
    pass


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        'title': "Login",
        'subtitle': "Welcome to website",
        'form': login_form,
    }

    print(request.user.is_authenticated)

    if login_form.is_valid():
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            print(user)
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO,
                                 "wrong user / pass")
            return redirect('/login')

    # print(login_form.cleaned_data)
    return render(request, "auth/login.html", context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('/login')
