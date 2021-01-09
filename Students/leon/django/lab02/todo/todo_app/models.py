from django.db import models
from django.conf import settings
from django.utils import timezone

class TodoItem(models.Model):
    task = models.CharField(max_length=200)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def publish(self):
        self.start = timezone.now()
        self.save()
    
    def finish(self):
        self.end = timezone.now()
        self.save()

    def complete(self):
        self.done = True
        self.save()

    
    
