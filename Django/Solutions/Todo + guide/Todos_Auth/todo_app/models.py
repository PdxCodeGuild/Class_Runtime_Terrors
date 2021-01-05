from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField(max_length = 500)
    status = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title