from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Todo
from django.contrib.auth.decorators import login_required


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer

##alternative option with permissions

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user = request.user) # filters todos by user

    # create the context dictionary to send the todos to the template
    context = {
        'todos': todos
    }

    return render(request, 'todos/todo_list.html', context) # context is sent to 'todos/list.html'


# view add a todo to the database. this view handles both GET and POST HTTP requests
@login_required
def add_todo(request):
    if request.method == 'GET':
        return render(request, 'todos/add.html')
    elif request.method == 'POST': 
        title = request.POST['title'] 
        text = request.POST['text'] 
        if (request.POST['status'] == 'False'):
            status = False
        else:
            status = True
      
        todo = Todo.objects.create(title = title, text = text, status = status, user= request.user)
        return redirect('list')

@login_required
def details(request, id):
    todo = Todo.objects.get(id = id)
    
    if todo.user == request.user:
         return render(request, 'todos/detail.html', {"todo": todo})
    return redirect('list')


@login_required
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

@login_required
def remove_todo(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect('list')