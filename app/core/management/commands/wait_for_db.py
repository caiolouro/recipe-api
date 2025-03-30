"""
To wait for the database to be available before starting the server
"""
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for the database to start...')
        db_started = False
        while db_started is False:
            try:
                self.check(databases=['default'])
                db_started = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database not started, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database started!'))
