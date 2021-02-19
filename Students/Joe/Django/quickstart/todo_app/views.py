from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

def todo_list(request):
    return HttpResponse('hello from todo List')