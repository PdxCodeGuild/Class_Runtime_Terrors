from django.db import models

class Image(models.Model):
    my_image = models.ImageField(upload_to='images/')