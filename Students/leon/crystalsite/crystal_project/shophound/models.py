from django.db import models
from django.urls import reverse

class RockShop(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, help_text='for URL; no spaces')
    address = models.CharField(max_length=100)
    website = models.URLField()
    hours = models.CharField(max_length=150)
    description = models.TextField()
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shophound-shop-detail', kwargs={'slug': self.slug})
