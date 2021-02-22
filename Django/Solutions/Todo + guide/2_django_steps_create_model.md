
## part 2: Create a Model


A model is a representation of your object in the Database. There are different ways to define a relationship between elements in the database:

- `OneToOneField` represents a [one-to-one relationship](https://docs.djangoproject.com/en/2.0/topics/db/examples/one_to_one/)
- `ForeignKey` represents a [many-to-one relationship](https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/)
- `ManyToManyField` represents a [many-to-many relationship](https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_many/)

* `Many-to-one relationships`. This can be the relationship between a car manufacturer and a car. A manufacturer can build different cars. But all the cars have one manufacturer in common.

```python

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...

```

* `Many-to-many relationships`. For example, if a Pizza has multiple Topping objects – that is, a Topping can be on multiple pizzas and each Pizza has multiple toppings – here’s how you’d represent that:

```python

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)
```

* `One-to-one relationships`  A OneToOneField would be like an Engine, where a Car object can have one and only one engine.`

```python
class Engine(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=25)
    engine = models.OneToOneField(Engine)

    def __unicode__(self):
        return self.name

```

1.Back to code! Open the *models.py* file inside of the todo_app folder. Inspect the following snippet and make your *models.py* file match:

    ```python
    from django.db import models


    class Todo(models.Model):
        title = models.CharField(max_length = 200)
        text = models.TextField(max_length = 500)
        status = models.BooleanField(default = False)

        TODO_TYPE = (
            ('p', 'personal'),
            ('s', 'school'),
            ('w', 'work'),
            ('f', 'family'),
            ('m', 'misc'),
        )

        todo_type = models.CharField(max_length = 1, choices = TODO_TYPE, blank = True, default = 'm')

        def __str__(self):
            return self.title
    ```

Once your *models.py* file matches, run `python manage.py makemigrations` and then `pythom manage.py migrate`.

makemigrations changes the configuration of the database

2. Create superuser

- run `python manage.py createsuperuser`

3. The shell

 (Making Queries, click [here](https://docs.djangoproject.com/en/3.1/topics/db/queries/))

- In the terminal run `python manage.py shell`
- run `from todo_app.models import Todo`
- run `Todo`, you should be returned a class
- run `Todo.objects.all()`, to see the content of your database. You should see `<QuerySet []>` if empty

Create a few entries:

- run `Todo.objects.create(title='laundry', text='do laundry', status=True)`
- run `Todo.objects.create(title='dishes', text='do dishes', status=False)`

You can also do (same as above):

- run `b = Todo(title='cooking', text='cooking', status=True)`
- run `b.save()`

Filtering:

- run `b = Todo.objects.filter(title = 'cooking')`
- run `b = Todo.objects.filter(id = 1)`

- run `a = Todo.objects.all()` to see all todos
- run `a[0]` to access the first element
- run `a[0].delete()` to delete the first element


## Part 4. Superuser

Exit the shell typing `exit()`. Let's discover the Admin panel and see all the todos that we have created. In todo_app > admin.py folder add the following:

```python
from django.contrib import admin

from . import models

admin.site.register(models.Todo)

```
