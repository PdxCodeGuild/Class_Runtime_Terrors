from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def user_register(request):
    if request.method == 'POST':
        new_user = User(
            username = request.POST['username'],
            email = request.POST['email'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name']
        )
        new_user.set_password(request.POST['password'])
        new_user.save()
        messages.success(request, 'User registered!')
        return redirect('login')
    return render(request, 'pages/register/register.html')


def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'pages/register/login.html')

def user_logout(request):
    logout(request)
    return redirect('dashboard')
