"""
Add permissions for Dashboard's different roles
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Add or Update permissions "

    def handle(self, *args, **option):
        pass
        
