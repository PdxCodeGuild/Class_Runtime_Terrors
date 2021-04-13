from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TodoItem(models.Model):
    item_name = models.CharField(max_length = 400)
    description = models.TextField()
    list_date = models.DateField()
    completion_date = models.DateField()
    

    def __str__(self):
        return self.item
# Create your models here.
