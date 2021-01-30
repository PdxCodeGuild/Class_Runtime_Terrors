from django.shortcuts import render

def index(request):
    return render(request, 'navigation/index.html')

def dashboard(request):
    return render(request, 'navigation/dashboard.html')
