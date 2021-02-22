from django.db import models

# Create your models here.

class FilesAdmin (models.Models):
    adminupload=models.FilesField(upload_to='media')
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title