from django.db import models
from django.utils import timezone
from django.conf import settings


class Urlss(models.Model):
    fullUrl = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    shortUrl = models.CharField(max_length=6)
