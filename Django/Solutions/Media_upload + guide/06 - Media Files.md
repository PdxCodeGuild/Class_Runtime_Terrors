

# Media Files

Before you begin:

- You may need to install pillow. If requested by Django, install pillow as a dependency in your virtual environment.

- I am using Bootstrap, so you may need to add it to your base.hmtml file

- Remember to add a **templates** folder with a base.html file and a static folder with JS and CSS files.

Web applications often allow users to upload files. This document covers how to allow users to upload files and save them alongside our application on a server. If you're using cloud hosting, you may want to look at alternative ways of storing files which separate the files from the application. Look at the official docs for more info: [File Uploads](https://docs.djangoproject.com/en/2.0/topics/http/file-uploads/), [ImageField](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ImageField), [FileField](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.FileField). You may also look at the different [mime types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types).


### 1: Specify the Save Location

In your project's `settings.py`, set the following variables.

```python
MEDIA_URL = '/uploaded_files/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')

```
### 2: Set up the Model

Given the settings shown here, files will be saved to `<project name>/uploaded_files/images`.

```python
from django.db import models
class MyModel(models.Model):
    my_image = models.ImageField(upload_to='images/')
```

### 3: Add a Route to Access the Files

In your project's `urls.py`, add the following line at the bottom. This will give the user the ability to access the file statically. Note that there's built-in access restriction, so anyone with a valid link will be able to view and download the associated file.

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('<you_app_name>.urls'))
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

### 4: Test

At this point, it's best to register your model with the admin panel, go to your admin panel, upload a file, make sure that the file appears in the directory you expected and that the link to the file works.

### 5: Add a View

- In your app folder > views.py add the following:

```python
from django.shortcuts import render, redirect
from . models import Image


def addImage(request):
    images = Image.objects.all()
    context = {
        "images": images
    }
    if request.method == 'GET':
        return render(request, 'pages/file.html', context)
    elif request.method == 'POST':
        my_image = request.FILES['my_image']
        Image.objects.create(my_image=my_image)
        return redirect('add_image')

```
- In your app folder, create a urls.py file and add the following:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.addImage, name = 'add_image')
]
```
- Inside your templates folder, add a folder `pages`. Inside the folder `pages` add the `file.html` page:

```html
{%extends 'base.html'%}
{%block content%}

<h1 class='text-center'> Upload images</h1>

<form enctype="multipart/form-data" action="{%url 'add_image'%}" id='author-form' class='mt-3' method="POST">
    {% csrf_token %}
    <label for="formFileMultiple" class="form-label">Multiple files input example</label>
    <input name="my_image" class="form-control" type="file" id="formFileMultiple" multiple>
    <button type="submit" class="btn btn-dark mt-3">Submit</button>
</form>


    <h1 class="text-center font-weight-light text-center text-lg-left mt-4 mb-5">Thumbnail Gallery</h1>
    <div class="container">
    {%for image in images%}
    <div>
        <a href="{{image.my_image.url}}">
            <img class="img-fluid img-thumbnail" src="{{image.my_image.url}}" alt="">
        </a>
    </div>
    {%endfor%}
</div>

{%endblock%}

```



