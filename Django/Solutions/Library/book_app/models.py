from django.db import models

class Author(models.Model):
    writer = (
        ('Ernest Hemingway','Ernest Hemingway'),
        ('Joan Didion','Joan Didion'),
        ('Ray Bradbury','Ray Bradbury'),
        ('Ayn Rand','Ayn Rand'),
        ('Gillian Flynn','Gillian Flynn'),
        ("Jane Austen","Jane Austen")
    )
    available_authors = models.CharField(max_length = 200, choices = writer, blank = True, unique=True)

    def __str__(self):
        return self.available_authors


class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return "%s %s" % (self.title, self.author)
