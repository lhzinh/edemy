from unittest.mock import patch

import pytest
from accounts.auth import ClerkUser
from accounts.models import User
from django.urls import reverse
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    user_list_url = reverse("user-list")

    def test_list_requires_authentication(self):
        with patch("accounts.auth.ClerkAuthentication.authenticate", return_value=None):
            response = APIClient().get(self.user_list_url)

        assert response.status_code == 401

    def test_list_only_exposes_the_authenticated_users_profile(self):
        own_user = User.objects.create_user(
            username="clerk_user_1",
            email="one@example.com",
            clerk_id="user_fake123",
        )
        User.objects.create_user(
            username="clerk_user_2",
            email="two@example.com",
            clerk_id="user_fake456",
        )
        clerk_user = ClerkUser(id="user_fake123", payload={})

        with patch(
            "accounts.auth.ClerkAuthentication.authenticate",
            return_value=(clerk_user, None),
        ):
            response = APIClient().get(self.user_list_url)

        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["id"] == own_user.id
        assert response.data[0]["email"] == "one@example.com"
        assert "password" not in response.data[0]

    def test_profile_endpoint_is_read_only(self):
        with patch(
            "accounts.auth.ClerkAuthentication.authenticate",
            return_value=(ClerkUser(id="user_fake123", payload={}), None),
        ):
            response = APIClient().post(
                self.user_list_url,
                {"email": "attacker@example.com", "clerk_id": "user_fake456"},
                format="json",
            )

        assert response.status_code == 405
