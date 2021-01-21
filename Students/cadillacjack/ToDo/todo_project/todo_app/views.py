from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, generics
from .serializers import TodoSerializer

class TodoView(generics.ListAPIView):
    serializer_class = TodoSerializer
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user = user)

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user = request.user)
    context = {
        'todos': todos
    }
    for todo in todos:
        print(todo)
    return render(request, 'todos/todo_list.html', context)

@login_required
def add_todo(request):
    if request.method == 'GET':
        return render(request, 'todos/add.html')
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        print(title, text)
        if (request.POST['status'] == 'False'):
            status = False
        else:
            status = True

    todo = Todo.objects.create(title = title, text = text, status = status, user = request.user)
    return redirect('list')

@login_required
def details(request, id):
    todo = Todo.objects.get(id = id)
    if todo.user == request.user:
        return render(request, 'todos/detail.html', {"todo":todo})
    return redirect('list')

@login_required
def update(request, id):
    todo = Todo.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'todos/update.html', {'todo':todo})
    elif request.method == 'POST':
        todo.title = request.POST['title']
        todo.text = request.POST['text']
        if (request.POST['status'] == "False"):
            todo.status = False
        else:
            todo.status = True
    todo.save()
    return redirect('details', todo.id)

@login_required
def remove_todo(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect('list')
