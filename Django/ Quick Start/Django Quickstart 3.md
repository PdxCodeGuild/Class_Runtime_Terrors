This guide covers the content in the folder **Forms and Links**.
## How to use a model and a database inside your template

Before continuing further, add a new URL in the my_app > urls.py folder:

```python
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('posts/', views.blog_posts, name = 'posts'),
    path('add/', views.add_post, name = 'add_posts')
]
```

- Go to the my_app folder > views.py, import the model and add a new function based view:

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog

def blog_posts(request):
    blogs = Blog.objects.all()  # gets all of the blog posts from the database and store them in a variable
  
    # creates the context dictionary to send the blog posts to the template
    context = {
       'blogs': blogs
    }
    return render(request, 'pages/posts.html', context)

def add_post(request):
    if request.method == 'GET': # if its a GET request, just display the add.html template
        return render(request, 'pages/add.html')
    elif request.method == 'POST': # if it's a POST request ..
        title = request.POST['title']   # get the title from the POST submission, this comes from a form
        text = request.POST['text']     # get the text from the POST submission, this comes from a form
        pub_date = request.POST['pub_date']
        # add the new blog post to the database. objects.create() automatically saves the new blog post for us so we
        # don't need a separate call to the save() method
        blogs = Blog.objects.create(title = title, text = text, pub_date = pub_date)
        return redirect('posts')
   
```

- In the Pages folder create a new page `posts.html` and add the following:

```html
{% extends 'base.html' %}
{% block content %}
<ul>
<a href="http://localhost:8000/add">add a blog post</a>
  {% for post in blogs %}
  <p>Title: {{ post.title }}</p>
  <p>ID: {{ post.id }}</p>
  <p>Description: {{ post.text }}</p>
  <p>Pub Date: {{post.pub_date}}</p>
  {% empty %}
  {% endfor %}
</ul>
{% endblock %}
```

## Add a form to create blog posts.

- In the Pages folder create a new page `add.html` and add the following:

```html
{% extends 'base.html' %}
{% block content %}
<form action="{% url 'add_posts' %}" method="POST">
    {% csrf_token %} title: <br />
    <input type="text" name="title" placeholder="enter todo title" /><br /><br />
    <textarea name="text" id="" cols="30" rows="10"></textarea><br />
    <input type="date" id="start" name="pub_date" value="2018-07-22" min="2018-01-01" max="2030-12-31">
    <br />
    <input type="submit" />
</form>
{% endblock %}

```
