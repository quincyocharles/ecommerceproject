from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def contact(request):
    return render(request, 'contact.html', {})


def product(request, pk):
    product = (Product.objects.get(id=pk))
    return render(request, 'product.html', {'product': product})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, ("You have successfully logged in! Welcome"))
            return redirect('home')
        else:
            messages.success(
                request, ("There was an error, please try again!"))
            return redirect('login')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)  # this will logout the user
    messages.success(
        request, ("You have been logged out! Thanks for stopping by😊"))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, ("Registration successful! Welcome"))
            return redirect('home')
        else:
            messages.success(
                request, ("Whoops! There was a problem registering. Please try again"))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})
