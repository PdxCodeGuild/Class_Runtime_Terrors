from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is pages_app/views.py/index')

def about(request):
    return HttpResponse('this is pages_app/views.py/about')

# Create your views here.
