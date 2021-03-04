from django.db import models

class Scanner(models.Model):
        text = models.TextField(max_length = 500)
        def __str__(self):
            return self.text 