# Django Quickstart 1 - Creating URLs, Views and Static folders.

## Set up Virtual Environment with PipEnv

If you do not have Pipenv, install it globally on your machine. In the terminal run 

`pip install pipenv`

I usually set Pipenv to the latest Python version available on my machine, so I run `pipenv --python 3.6`

Then I run: `pipenv install django`

## Run server

-To verify that Django was installed correctly, run the server. In the terminal run `python manage.py runserver` (if you are using Python 3 you may run `python3 manage.py runserver`)

-To exit the server, press CONTROL + C.

## Create a project.

- Create a site/project: `django-admin startproject <project_name> .` Remember to add a . (dot at the end, after the project name)

## Create an app inside the project.

- Create an app: `python manage.py startapp <app-name>`
- Add your app to the `INSTALLED_APPS` in `settings.py`

   ```python
   INSTALLED_APPS = [
        .....
       '<app-name>',
   ]
   ```
-Add `import os` at the top of the Settings.py page if you do not see it there.

## Setup your static files. Base.HTML, CSS and Javascript files.
 
1. create a _templates_ template directory at the same level as the _project_name_ directory. **It should not** be nested inside another directory. Inside of the templates folder create a folder called _pages_. Pages will hold basic pages that display a home page, an about page, etc. Inside the folder _pages_, create a page named `home.html`that has the following:

```html
{% extends 'base.html' %}
{% block content %}
    <h1>Home</h1>
{% endblock %}
```

2. Create another page in the same folder named `about.html`:

```html
{% extends 'base.html' %}
{% block content %}
    <h1>About</h1>
{% endblock %}
```

3. Create a static directory at the same level as the _project_name_ directory. _static_ **should not** be nested inside another directory. Inside of _static_, create two directories, _css_ and _js_. Inside of _css_ create a **file** _site.css_. inside of _js_ create a **file** _main.js_. inside of _site.css_ add the following css:

   ```css
   h1 {
     color: firebrick;
   }
   ```

   inside _main.js_ add the following:

   ```javascript
   console.log("hello from main.js");
   ```

4. We now need to tell django where to find our templates and static files. Open up _settings.py_ in the _my_project_name_ folder. Modify the templates section to look like the following snippet. specifically you need to modify the 'DIRS' line by adding `os.path.join(BASE_DIR, 'templates')`.

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

Next, add `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]` to the bottom of the _settings.py_ file below the line specifying `STATIC_URL`.

## Adding a base HTML file.

In root directory of the **templates** folder, add a base.html file:

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

## Create a View

- In your app's `views.py`:
```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')
```

## Create a Route to the Views

- Create a `urls.py` inside your app folder
- Add a route in your app's `urls.py` which points to the the view
- Add an `app_name` to be able to look up paths when you render a template

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about')
]
```

## Hook these URLs and views to the Project URLs

- Add a route in your project's `urls.py` which points to the app's `urls.py` using `include`

```python
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<path>/', include('<appname>.urls')) # Note: all your app urls will start with this path
]
```


