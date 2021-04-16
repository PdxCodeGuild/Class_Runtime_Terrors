from django.db import models

class Ushort(models.Model):
    url_name = models.CharField(max_length = 200)
    shortened_url = models.CharField(max_length = 10)

