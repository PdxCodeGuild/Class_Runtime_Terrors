from django.db import models
from django.urls import reverse

class HoundSite(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, help_text='for URL; no spaces')
    address = models.CharField(max_length=100)
    rocks = models.TextField()
    notes = models.TextField()
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rockhound-site-detail', kwargs={'slug': self.slug})

        