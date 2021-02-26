from django.db import models
from django.conf import settings
from django.db import models
from django_resized import ResizedImageField
from PIL import Image
from django.utils import timezone



# Create your models here.
# class Image (models.Model):
#     image = models.ImageField(null = True, blank = True, upload_to ='img/%y')

class Album (models.Model):
    album_cover = models.ImageField(null = True, blank =True, upload_to ='galleries/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, blank =True, on_delete=models.CASCADE)
    text = models.TextField(null = True, blank =True)
    created_date = models.DateTimeField(default=timezone.now)

    # photographer = models.CharField()
    # image = ResizedImageField(null = True, blank =True, upload_to='galleries/')

    # def save (self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.weight >300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    # def _str__(self):
    #     return self.image.name
    def _str__(self):
        return self.author

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
