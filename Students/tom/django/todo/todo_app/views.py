from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo


def todo_list(request):
    # gets all of the todos from the database and store them in todos
    todos = Todo.objects.all()

    # create the context dictionary to send the todos to the template
    context = {
        'todos': todos
    }

    return render(request, 'todos/todo_list.html', context)
# context is sent to 'todos/todo_list.html'


def add_todo(request):
    if request.method == 'GET':  # if its a GET request, just display the todos/add.html template
        return render(request, 'todos/add.html')
    elif request.method == 'POST':  # if it's a POST request ...
        # get the title from the POST submission, this comes from a form
        title = request.POST['title']
        # get the text from the POST submission, this comes from a form
        text = request.POST['text']
        # check the status because it's a string and booleans are not strings
        if (request.POST['status'] == 'False'):
            status = False
        else:
            status = True
        # add the new todo to the databse. objects.create() automatically saves the new todo for us so we
        # don't need a separate call to the save() method
        todo = Todo.objects.create(title=title, text=text, status=status)
        return redirect('list')


def details(request, id):
    todo = Todo.objects.get(id=id)

    return render(request, 'todos/detail.html', {'todo': todo})


def update(request, id):
    todo = Todo.objects.get(id=id)
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


# view to remove a specific todo from the database specified by its id
def remove_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('list')
