from django.test import TestCase
# This function reflects any user model changes, Django default or custom
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_when_user_has_email_and_password(self):
        email = 'test@example.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_when_user_has_denormalized_email(self):
        emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for input_email, expected_email in emails:
            user = get_user_model().objects.create_user(email=input_email, password='testpassword')
            self.assertEqual(user.email, expected_email)

    def test_when_user_has_no_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='', password='testpassword')
