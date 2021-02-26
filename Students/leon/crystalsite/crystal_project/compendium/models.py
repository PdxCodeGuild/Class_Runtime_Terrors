from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('compendium-tag-detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('compendium-tag-update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('compendium-tag-delete', kwargs={'slug': self.slug})

class Crystal(models.Model):
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config')
    description = models.TextField()
    image = models.ImageField(upload_to="galleries", blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('compendium-crystal-detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('compendium-crystal-update', kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        return reverse('compendium-crystal-delete', kwargs={'slug': self.slug})
