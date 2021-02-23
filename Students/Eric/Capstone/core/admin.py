from django.contrib import admin
from .models import Book, Event, Ask

# Register your models here.

admin.site.register(Book)
admin.site.register(Event)
admin.site.register(Ask)
