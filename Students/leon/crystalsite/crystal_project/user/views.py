from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

def new_user(request):
    if request.method == "POST":
        new_user = User(
            username = request.POST['username'],
            email = request.POST['email'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
        )
        new_user.set_password(request.POST['password'])
        new_user.save()
        messages.success(request, 'New user registered!')
        return redirect('login')
    return render(request, 'user/signup.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('blog-post-list')
    return render(request, 'user/login.html')

def user_logout(request):
    logout(request)
    return redirect('blog-post-list')

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            message.success(request, 'Password updated!')
            return redirect('blog-post-list')
        else:
            messages.error(request, 'Please correct errors.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/password_change_form.html', {'form': form})

def register(request):
    return render(request, 'user/register.html')
