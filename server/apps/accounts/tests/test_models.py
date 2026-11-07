import pytest
from accounts.models import User


@pytest.mark.django_db
class TestUsers:
    def test_user_model(self, user):
        assert isinstance(user, User)
        assert user.is_superuser is False
