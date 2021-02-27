import sys
import requests
import socket
from django.shortcuts import render,redirect
from django.http import HttpResponse
from subprocess import run,PIPE
from . models import Scanner
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def ports(request):
    return render(request, 'pages/ports.html')

# Python Port Scanner Script
def external(request):
    ip = request.POST.get('run_script')
    input= request.POST.get('run_script')
    s = socket.socket(2, 1)
    def scan(ip, port):
        try:
            s.connect((ip, port))
            return True
        except:
            return None
    myScan = []
    # for port in range(0 to 65353):
    # for port in range(20,30): # 10.0.0.192
    for port in range(45,55): # 10.0.0.1
        value = scan(ip, port)
        if value == None:
            print("Port not opened on %d" % port)
        else:            
            print("Port opened on %d" % port)
            myScan.append(port)
    context = {"myScan":myScan}    
    return render(request,'pages/scan.html',context)

# Scan Page, requires login to work     
@login_required
def scan(request):
    return render(request, 'pages/scan.html')  

# Clear Scan Page
def r_script(request):
    print("\nRun clear page\n")
    return render(request, 'pages/scan.html')

# Register User
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')     
    else:
        form = UserCreationForm()
        return render(request, 'pages/register.html', {'form': form})

# Login Page
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            return render(request, 'pages/scan.html')
        else: 
            form = AuthenticationForm()
            return render(request, 'pages/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'pages/login.html', {'form': form})
# Log out 
def logout(request):
    auth_logout(request)
    return render(request,"logout");