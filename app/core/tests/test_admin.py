from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="mypassword"
        )
        self.client.force_login(self.superuser)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="myweakpassword",
            name="Regular user"
        )

    def test_when_list_then_list_regular_user(self):
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
