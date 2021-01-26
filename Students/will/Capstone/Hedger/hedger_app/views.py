from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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
            first_name = request.POST['first_name'],
            
            )
            new_user.set_password(request.POST['password'])
            new_user.save()
            messages.success(request, 'User registered!')
            return redirect('login')
    return render(request, 'pages/signup.html')

def login(request):
    if request.method == 'POST':
        user = authenticate(request, request.POST['username'], password = request.POST['password'])
        if user is not None: 
            login(request,user)
            return redirect('account')
    return render (request, 'pages/login.html')


# def user_login(request):
#     if request.method == 'POST':
#         user = authenticate(
#             request,
#             username = request.POST['username'],
#             password = request.POST['password']
#         )
#         if user is not None:
#             login(request, user)
#             return redirect('posts')
#     return render(request, 'register/login.html')