from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import API
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def user_register(request):
    if request.method == 'POST':
        users = User.objects.all().filter(username=request.POST['username']).exists()
        if users:
            messages.warning(request, 'User already exists!')
        else:
            new_user = User(
                username = request.POST['username'],
                email = request.POST['email'],
                # first_name = request.POST['first_name'],
                # last_name = request.POST['last_name']
        )
            new_user.set_password(request.POST['password'])
            new_user.save()
            messages.success(request, 'User registered!')
            return redirect('login')
    return render(request, 'pages/signup.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('api')
        else:
            return redirect('signup')
    return render(request, 'pages/login.html')

def api(request):
    return render(request, 'pages/api.html')

def user_logout(request):
    logout(request)
    return redirect('home')