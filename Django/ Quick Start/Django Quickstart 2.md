This guide covers the content in the folder **Model**

## Create Models

Go to the my_app folder and inside the models.py file add a model. The following is an example of a **many to one** relationship model:

```python
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
        title = models.CharField(max_length = 200)
        text = models.TextField(max_length = 500)
        pub_date = models.DateField()
        user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)

        def __str__(self):
            return self.title
```

- Stage your migrations: `python manage.py makemigrations <appname>`
- Perform migrations (synchronize your models with your database): `python manage.py migrate`

2. Create superuser

- run `python manage.py createsuperuser`

3. The shell

 (Making Queries, click [here](https://docs.djangoproject.com/en/3.1/topics/db/queries/))

- In the terminal run `python manage.py shell`
- run `from my_app.models import Blog`
- run `Blog`, you should be returned a class
- run `Blog.objects.all()`, to see the content of your database. You should see `<QuerySet []>` if empty

Create a few entries:

- run `Blog.objects.create(title='I made my kittens bark', text='lorem ipsum', pub_date='2009-11-12')`
- run `Blog.objects.create(title='The economy of the 20th century', text='another lorem ipsum', pub_date='2020-01-12')`

You can also do (same as above):

- run `b = Blog.objects.create(title='I made my kittens bark', text='lorem ipsum', pub_date='2009-11-12')`
- run `b.save()`

Filtering:

- run `b = Blog.objects.filter(title = 'I made my kittens bark')`
- run `b = Blog.objects.filter(id = 1)`
- run `Blog.objects.filter(title__startswith='I made')`

- run `a = Blog.objects.all()` to assign all posts to a variable
- run `a` to see all blog posts
- run `a[0]` to access the first element
- run `a[0].delete()` to delete the first element


## Part 4. Superuser

Exit the shell typing `exit()`. Let's discover the Admin panel and see all the blog posts that we have created. In my_app > admin.py page add the following:

```python
from django.contrib import admin

from . import models

admin.site.register(models.Blog)

```
- In the terminal, start the server and run `python manage.py runserver`
- run `python manage.py createsuperuser`
- Go to` http://localhost:8000/admin/` to explore the page and add more blog posts.