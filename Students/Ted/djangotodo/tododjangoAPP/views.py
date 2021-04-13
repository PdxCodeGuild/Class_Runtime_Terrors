from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def item(request):
    return render(request. 'pages/add.html')

def detail(request, todo_item_id):
    todo_item = get_object_or_404(TodoItem, pk=todo_item_id)
    return render(request, 'todoapp/detail.html', {'todo_item': todo_item})

def 

# Create your views here.
