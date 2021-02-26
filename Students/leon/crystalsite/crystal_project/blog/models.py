from django.db import models
from django.urls import reverse
from compendium.models import Crystal, Tag
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63,
        help_text='use lowercase, alpha-numeric characters and replace all spaces with underscores',
        unique_for_month='pub_date'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    pub_date = models.DateField(
        'date published',
        auto_now_add=True
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        help_text='hold CTRL to select more than 1 tag',
        related_name='blog_posts'
        )
    crystals = models.ManyToManyField(
        Crystal,
        blank=True,
        help_text='hold CTRL to select more than 1 crystal',
        related_name='blog_posts'
        )

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

    def __str__(self):
        return "{} on {}".format(
            self.title, 
            self.pub_date.strftime('%Y-%m-%d')
        )
    
    def get_absolute_url(self):
        return reverse('blog-post-detail', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    def get_update_url(self):
        return reverse('blog-post-update', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})
    
    def get_delete_url(self):
        return reverse('blog-post-delete', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    def get_archive_year_url(self):
        return reverse('blog-post-archive-year', kwargs={'year': self.pub_date.year})

    def get_archive_month_url(self):
        return reverse('blog-post-archive-month', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month})