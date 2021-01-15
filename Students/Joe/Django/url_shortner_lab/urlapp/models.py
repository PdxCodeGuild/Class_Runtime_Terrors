from django.db import models

# Create your models here.
class URL_alter (models.Model):
    long_url = models.CharField(max_length=800)
    short_url = models.CharField(max_length=800)

    def __str__(self):
        return self.long_url
