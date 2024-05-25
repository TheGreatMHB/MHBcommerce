from django.shortcuts import render, redirect
from django.http import HttpResponse
from MHBCommerce.forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
    register_form = RegisterForm(request.POST or None)
    context = {
        'form': register_form
    }
    if register_form.is_valid():
        print(register_form.cleaned_data)
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        new_user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        print(new_user)

        messages.success(
            request, "Account Created successfully for " + username)
        return redirect('/login')
    else:
        messages.error(request, "Everything is fucked ...")

    return render(request, "auth/register.html", context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        'title': "Login",
        'subtitle': "Welcome to website",
        'form': login_form,
    }

    print(request.user.is_authenticated)

    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            messages.success(
                request, "Logged in successfully")
            return redirect('/')

        else:
            messages.error(request, "Everything is fucked ...")
            return redirect('/login')

    return render(request, "auth/login.html", context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('/login')
