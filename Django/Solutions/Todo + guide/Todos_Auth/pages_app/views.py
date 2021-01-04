from django.shortcuts import render, redirect
from django.http import HttpResponse 

def index(request):
    return render(request, "pages/index.html")
# Create your views here.
def about(request):
    return render(request, "pages/about.html")
