from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    def test_when_check_ready(self, patched_check):
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(database=['default'])

    # Beware of patched objects arguments order: first is sleep because it is the "closest" decorator then the outer check one
    @patch('time.sleep')
    def test_when_check_delayed(self, patched_sleep, patched_check):
        # First two calls to check raise Psycopg2Error, 4 raise OperationalError and the last one works
        patched_check.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 4 + [True]
        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 7)
        patched_check.assert_called_with(database=['default'])