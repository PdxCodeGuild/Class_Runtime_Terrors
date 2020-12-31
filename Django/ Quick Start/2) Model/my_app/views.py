from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Home')

# def about(request):
#     return HttpResponse('About')

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')
