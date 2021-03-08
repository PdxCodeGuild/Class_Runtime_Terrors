from django.db import models


class Url_Shortener(models.Model):
    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=20)
    output_url = models.CharField(max_length=200)

    def __str__(self):
        return self.output_url
