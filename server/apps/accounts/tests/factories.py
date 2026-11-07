import factory
from accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """User factory."""

    class Meta:
        model = User
