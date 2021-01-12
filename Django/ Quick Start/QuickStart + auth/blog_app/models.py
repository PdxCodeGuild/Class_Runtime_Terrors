from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length= 200)
    text = models.CharField(max_length=200)
    pub_date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True , blank = True)

    def __str__(self):
        return self.title
