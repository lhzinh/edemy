from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    clerk_id = models.CharField(
        max_length=255, unique=True, db_index=True, blank=True, null=True
    )
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
    image = models.ImageField(upload_to="avatars/", null=True, blank=True)
    # is_verified = models.BooleanField(
    #     _("email verified"),
    #     default=False,
    #     help_text=_("Designates whether the user has verified their email."),
    # )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: ClassVar[list[str]] = ["username", "first_name", "last_name"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        # Add indexes for common queries
        indexes: ClassVar[list[models.Index]] = [
            models.Index(fields=["email"]),
            models.Index(fields=["is_active"]),
        ]
