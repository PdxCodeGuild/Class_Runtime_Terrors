  
from django.db import models
from django.utils.timezone import now

from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Ask(models.Model):
    name = models.CharField(max_length=100, null=False)
    request = models.CharField(max_length=100, null=False)    
    date = models.DateTimeField(default=now, editable=True)

class Book(models.Model):
    number = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100,null=False)
    pdf = models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
