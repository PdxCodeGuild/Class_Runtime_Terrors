from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import TodoItem
from .forms import TaskForm

def todo(request):
    tasks = TodoItem.objects.all()
    return render(request, 'todo_app/todo.html', {'tasks': tasks})

def post_new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('todo')
    else:
        form = TaskForm()
    return render(request, 'todo_app/post_edit.html', {'form': form})

def post_detail(request, pk):
    task = get_object_or_404(TodoItem, pk=pk)
    return render(request, 'todo_app/post_detail.html', {'task':task})

def post_edit(request, pk):
    task = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_app/post_edit.html', {'form': form})
            