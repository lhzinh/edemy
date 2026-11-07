import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from apps.accounts.tests.factories import UserFactory

register(UserFactory)


@pytest.fixture
def api_client():
    return APIClient()
