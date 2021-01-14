
## part 1: django initial setup

0. create a directory for your project
1. `cd` into the directory you just created, then create your virtual environment using `pipenv`
   ```python
   pipenv shell
   ``` 
2. install django and ensure it was installed

   ```python
   pipenv install django
   pip list
   ```

   the output from the `pip list` command should be similar to the following (the output will depend on the version of django you installed):

   | Package    | Version |
   | ---------- | ------- |
   | asgiref    | 3.2.3   |
   | Django     | 3.0     |
   | pip        | 19.3.1  |
   | pytz       | 2019.3  |
   | setuptools | 42.0.2  |
   | sqlparse   | 0.3.0   |
   | wheel      | 0.33.6  |

3. create a django project with the command<br>
   `django-admin startproject my_project_name .`

4. test to make sure the server runs<br>
   `python3 manage.py runserver`<br>
  
   if everything was done correctly, you should see the default server page with the animated rocket.
   [](./django_scrnsht.png)

## part 2: todo list setup. Adding views, URLS and static pages.

There are many ways to approach a django project. This is just one version of how i do it. It's a general pattern i usually follow, but there are times when i deviate from this for no other reason than my thought process may not be the same from app to app. Many of the steps are purely organizational and can be changed to fit whatever organizational scheme makes the most sense to you.

1. Exit the server by pressing control + c. Create an app with the command<br>
   `python3 manage.py startapp todo_app` <br>
   `python3 manage.py startapp pages_app`

   go into your _my_project_name/settings.py_ file and install your apps. Add the name of your app to the list of installed apps like so:

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'pages_app',
       'todo_app',
   ]
   ```

2. create a _templates_ template directory at the same level as the _to_do_app_ and _my_project_name_ directories. **It should not** be nested inside another directory. Inside of the templates folder create a folder called _pages_ and another called _todos_. Pages will hold basic pages that display a home page, an about page, etc. todos will hold pages that have something to do with our todo_list app.

3. create a static directory at the same level as the _to_do_app_, _templates_, and _my_project_name_ directories. _static_ **should not** be nested inside another directory. Inside of _static_, create two directories, _css_ and _js_. inside of _css_ create a **file** _site.css_. inside of _js_ create a **file** _main.js_. inside of _site.css_ add the following css:

   ```css
   h1 {
     color: firebrick;
   }
   ```

   inside _main.js_ add the following:

   ```javascript
   console.log("hello from main.js");
   ```

4. We now need to tell django where to find our templates and static files. Open up _settings.py_ in the _my_project_name_ folder. modify the templates section to look like the following snippet. specifically you need to modify the 'DIRS' line by adding `os.path.join(BASE_DIR, 'templates')`.

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

   next, add `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]` to the bottom of the _settings.py_ file below the line specifying `STATIC_URL`.

**extra step** add `import os` at the top of the page if you do not see it there

5.  Let's create a view for the app. Go to the 'todo_app' and add the following code to your \_views.py* files in todo_app.

    _todo_app/views.py_

    ```python
        from django.shortcuts import render, redirect
        from django.http import HttpResponse

        def todo_list(request):
            return HttpResponse('hello from todo List')
    ```

6.  We need to tell Django to return this once it hits a specific endpoint. To do it, we need to create a _urls.py_ file inside the todo_app folder.

        _todo_app/urls.py_

     ```python
       from django.urls import path
       from . import views

        urlpatterns = [
        path('', views.todo_list, name = 'list'),
        ]
    ```

7.  At this point we need to _connect everything to a specific URL_. We are basically saying to Django : "once you hit http://127.0.0.1:8000/todo/ you return a *view* from its *URL*. Let's go to the app *project folder, click \_urls.py* and import the view.

```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('todos/', include('todo_app.urls')),
       path('admin/', admin.site.urls),
   ]
```
7. Repeat the same steps for the pages_app this time. Enter the folder pages_app. First create a view, then add a urls.py file.

*pages_app/views.py*
```python
    from django.shortcuts import render
    from django.http import HttpResponse

    def index(request):
        return HttpResponse('hello from the index/home view')

     def about(request):
        return HttpResponse('hello from the about view')
```

  *pages_app/urls.py*
```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name = 'home'),
        path('about/', views.about, name = 'about'),
    ]
```

8. Go back to the Todo_project folder and add the *pages.urls* endpoint.

```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('', include('pages_app.urls')),
       path('todos/', include('todo_app.urls')),
       path('admin/', admin.site.urls),
   ]
```

9. We are able to return a simple message included in a string. This isn't that efficient. We can return entire pages. You'll need to think about how you want the user to interact with your app to determine what templates you'll need. Since it depends on how you want your app laid out, I'll show you a simple setup for a base template called _base.html_, and how you can extend that base template with another template.

   _templates/base.html_

   ```html
       {% load static %}
       <!DOCTYPE html>
       <html lang="en">
       <head>
           <meta charset="UTF-8">
           <meta name="viewport" content="width=device-width, initial-scale=1.0">
           <meta http-equiv="X-UA-Compatible" content="ie=edge">
           <link rel="stylesheet" href="{% static 'css/site.css' %}">
           <title>welcome</title>
       </head>
       <body>
           {% block content %}
           {% endblock %}
           <script src="{% static 'js/main.js' %}"></script>
       </body>
       </html>
   ```

   _templates/pages/index.html_

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>hello from the index template</h1>
   {% endblock %}
   ```

   _templates/todos/list.index.html_

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>hello from the todo list template</h1>
   {% endblock %}
   ```

10. Go back to todo_app > views.py and change:

```python
def todo_list(request):
    return HttpResponse('hello from todo')
```
To 

```python
def todo_list(request):
    return render(request, 'todos/todo_list.html')
```

10. Go back to pages > views.py and change everything to:

```python

def index(request):
    return render(request, "pages/index.html")

def about(request):
    return render(request, "pages/about.html")

```