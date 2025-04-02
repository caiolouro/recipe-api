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