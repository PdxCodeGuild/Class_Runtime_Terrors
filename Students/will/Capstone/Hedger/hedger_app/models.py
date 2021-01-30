from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class API(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    api_key = models.CharField(max_length=50)
    secret_api = models.CharField(max_length=50)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.api_key