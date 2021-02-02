from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=60)
    album_cover = models.ImageField(upload_to="album_thumbnails/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    #above names the object to make trouble shooting easier


class Image(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to="galleries")
    Album = models.ForeignKey(User, on_delete = models.CASCADE, blank=True)

    def __str__(self):
        return self.image.name