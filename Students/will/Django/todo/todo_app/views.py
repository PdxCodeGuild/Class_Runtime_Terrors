from django.shortcuts import render, redirect
from django.http import HttpResponse

def todo_list(request):
    return render(request, 'todos/todo_list.html')