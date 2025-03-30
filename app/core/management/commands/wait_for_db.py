"""
To wait for the database to be available before starting the server
"""
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        pass