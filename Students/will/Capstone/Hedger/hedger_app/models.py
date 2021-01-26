from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
        username = models.CharField(max_length = 200)
        text = models.TextField(max_length = 500)
        pub_date = models.DateField()
        user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)

        def __str__(self):
            return self.title