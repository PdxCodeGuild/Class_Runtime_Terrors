from django.db import models

class URL_Shortener(models.Model):
        url_name = models.CharField(max_length=800)
        shortened_url = models.CharField(max_length=800)

        def __str__(self):
            return self.url_name



