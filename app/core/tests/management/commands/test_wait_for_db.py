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
        patched_check.assert_called_once_with(databases=['default'])

    # Beware of patched objects arguments order:
    # First is sleep because is the "closest" decorator then the outer check
    @patch('time.sleep')
    def test_when_check_delayed(self, patched_sleep, patched_check):
        # First two calls to check raise Psycopg2Error
        # Then 4 raise OperationalError
        # Then the last one works
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 4 + [True]
        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 7)
        patched_check.assert_called_with(databases=['default'])
