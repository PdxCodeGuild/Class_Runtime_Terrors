## Use the Model inside your template

0. Go back to the Todo_app folder > views.py
1. Import the model created with:
   ```python
   from .models import Todo
   ```
2. You want to start to retrieve items from the database using the following syntax:

```python
   todos = Todo.objects.all()
      context = {
        'todos': todos
    }
```

The final format will be:

```python

def todo_list(request):
   todos = Todo.objects.all()  # gets all of the todos from the database and store them in todos

   # create the context dictionary to send the todos to the template
   context = {
       'todos': todos
   }

      return render(request, 'todos/todo_list.html', context)
# context is sent to 'todos/todo_list.html'
```

3. You need to start displaying all the tasks in the template, since you passed in the object to it. Go to the templates folder > todos > todo_list.html and add under `{% extends 'base.html' %}`:

```html
{% block content %}
<a href="http://localhost:8000/todo/add">add task</a>
<ul>
  {% for todo in todos %}
  <p>Title: {{ todo.title }}</p>
  <p>ID: {{ todo.id }}</p>
  <p>Description: {{ todo.text }}</p>
  {% empty %}
  <p>you have nothing to do.</p>
  {% endfor %}
</ul>
{% endblock %}
```

4. Let's add more Todos! Go to the templates folder > todos and add a page named add.html.

In that page, add the following under `{% extends 'base.html' %}`:

```html
{% block content %}
<form action="{% url 'add' %}" method="POST">
  {% csrf_token %} title: <br />
  <input type="text" name="title" placeholder="enter todo title" /><br />
  description:<br />
  <textarea name="text" id="" cols="30" rows="10">
type todo description here</textarea
  ><br />
  status: <br />
  <select name="status">
    <br />
    <option value="True">True</option>
    <option value="False">False</option>
  </select>
  <br />
  <input type="submit" value="add" />
</form>
{% endblock %}
```

5. We need to connect the page to its endpoint. In todo_app views.py add :

```python
def add_todo(request):
    if request.method == 'GET': # if its a GET request, just display the todos/add.html template
        return render(request, 'todos/add.html')
    elif request.method == 'POST': # if it's a POST request ...
        title = request.POST['title']   # get the title from the POST submission, this comes form a form
        text = request.POST['text']     # get the text from the POST submission, this comes form a form
        if (request.POST['status'] == 'False'): # check the status because it's a string and booleans are not strings
            status = False
        else:
            status = True
        # add the new todo to the databse. objects.create() automatically saves the new todo for us so we
        # don't need a separate call to the save() method
        todo = Todo.objects.create(title = title, text = text, status = status)
        return redirect('list')
```

6. In todo_app urls.py add:

```python
    path('about/', views.about, name='about')
```

It should look like this:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name='about')
]
```

7. Let's say that we want to click on each todo and display a page with 2 options: "update" and "delete". To do this, we'll need to create a link to each specific todo using its unique ID. Remember, each time you create an element in the database it has an ID specific to that element.

- In templates > todos add a page `detail.html` with the following:

```html
{% extends 'base.html' %} {% block content %}
<p>title: {{ todo.title }}</p>
<p>description: {{ todo.text }}</p>
<p>status: {{ todo.status }}</p>
<a href="">update</a>
<a href="">remove</a>
{% endblock %}
```

- Let's return this page by a view. inside the todo_app folder go to views.py page and add:

```python

def details(request, id):
    todo = Todo.objects.get(id = id)

    return render(request, 'todos/detail.html', {"todo": todo})

```

- Connect the view vith its URL. In the todo_app folder go to urls.py and add:

```python
    path('details/<int:id>', views.details, name = 'details'),
```

The `<int:id>` expects an integer after the link. The integer is the ID of the todo.

- Now grab an id and add it at the end of the following url:

example: `http://localhost:8000/todo/details/13`

But how can we have dinamic links in the list.html page? Go back to that page, remove everything and add this:

```html
{% extends 'base.html' %} {% block content %}
<a href="http://localhost:8000/todo/add">add task</a>

{% for todo in todos %}
<p>
  <a href="http://localhost:8000/todo/details/{{ todo.id }}"
    >{{ todo.title }}</a
  >
</p>
<p>ID: {{ todo.id }}</p>
<p>Description: {{ todo.text }}</p>
{% empty %}
<p>you have nothing to do.</p>
{% endfor %} {% endblock %}
```

Right now you should be able to see a view of each todo element every time you click on the title.

8. Now we want to add the functionality to update or delete each todo. 

- To update a todo, we'll need to implement a form. Let's start with creating the page "update.html" inside Templates > todos. Add the following:

```html
{% extends 'base.html' %}

{% block content %}
<form action="{% url 'update' todo.id %}" method="POST">
    {% csrf_token %}
    title: <br> <input type="text" name="title" value="{{ todo.title }}"><br>
    description:<br> <textarea name="text" id="" cols="30" rows="10">{{ todo.text }}</textarea><br>
    status: <br> <select name="status"><br>
        <option value="True">True</option>
        <option value="False" selected>False</option>
      </select> 
      <br>
    <input type="submit" value="update">
</form>
{% endblock %}
```

- Let's connect this template to its view and URL. In the folder todo_app views.py add:

```python
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
```
- In the todo_app > urls.py page add:

```python
    path('update/<int:id>', views.update, name = 'update'),
```
- Back to the detail.html page add the following href for the update "a" tag:

```html
<a href="{% url 'update' todo.id %}">update</a>
```
You can also add the following to go back one step

```html
<a href ="http://localhost:8000/todo/">Back to main todo list</a>
```

9. Let's implement a function to remove a todo. This time we do not need much, we just need to ask the database to remove something. Let's implement the function in the todo_app > views.py page:

```python
# view to remove a specific todo from the database specified by its id
def remove_todo(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect('list')
```

- Add the related URL. Go to todo_app urls.py:

```python
path('delete/<int:id>', views.remove_todo, name = 'remove')
```
- Add the following in the detail.html page:

```html
    <a href="{%url 'remove' todo.id %}">remove</a>

```



