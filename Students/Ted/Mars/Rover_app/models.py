from django.db import models
from django.contrib.auth.models import User



class MediaModel(models.Model):
    my_image = models.ImageField(upload_to='images/')

class Image(models.Model):
    sol = models.IntegerField()
    num = models.IntegerField(default = 0)
    image_link = models.TextField(max_length = 500)
    
    def __str__(self):
        return str(self.sol)

