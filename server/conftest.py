from functools import lru_cache
from unittest.mock import patch

import pytest
from clerk_backend_api import Clerk
from clerk_backend_api.security.types import AuthStatus, RequestState
from django.conf import settings
from rest_framework.test import APIClient

from apps.accounts.auth import ClerkUser


@pytest.fixture
def api_client():
    return APIClient()


def _fake_auth():
    payload = {"sub": "user_fake123", "sid": "sess_fake"}
    state = RequestState(status=AuthStatus.SIGNED_IN, payload=payload)
    user = ClerkUser(id=payload["sub"], payload=payload)
    return (user, state)


@pytest.fixture(autouse=True)
def _override_auth():
    with patch("accounts.auth.ClerkAuthentication.authenticate") as mock:
        mock.return_value = _fake_auth()
        yield mock


@lru_cache
def get_clerk() -> Clerk:
    return Clerk(bearer_auth=settings.CLERK_SECRET_KEY)


@pytest.fixture(scope="session")
def sdk_client():
    client = get_clerk()
    yield client
    # Teardown step
    client.close()
