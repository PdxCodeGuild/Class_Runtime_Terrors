from django.shortcuts import render, redirect
from django.http import HttpResponse 
# Create your views here.
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todos = Todo.objects.all()  # get all of the todos from the database and store them in todos

    # create the context dictionary to send the todos to the template
    context = {
        'todos': todos
    }

    return render(request, 'todos/todo_list.html', context) # context is sent to 'todos/list.html'


# view add a todo to the database. this view handles both GET and POST HTTP requests
def add_todo(request):
    if request.method == 'POST': # if it's a POST request ...
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            todo = form.cleaned_data.get('title')
            return redirect('list')
    else:
            form = TodoForm()
    return render(request, 'todos/add.html', {"form": form})

# view to get retrieve a specific todo from the database and send it to the 'todos/detail.html' view
def details(request, id):
    todo = Todo.objects.get(id = id)

    return render(request, 'todos/detail.html', {"todo": todo})


def update(request, id):
    todo = Todo.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'todos/update.html', {'todo': todo})
    elif request.method == 'POST':
        todo.title = request.POST['title']
        todo.text = request.POST['text']
        if (request.POST['status'] == 'False'):
            todo.status = False
        else:
            todo.status = True
        todo.save()
        return redirect('details', todo.id)

def remove_todo(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect('list')