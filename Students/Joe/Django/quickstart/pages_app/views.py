from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello from the index/home view')

    def about(request):
    return HttpResponse('hello from the about view')