from django.db import models

class Short_URL(models.Model):
    original_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=255)
