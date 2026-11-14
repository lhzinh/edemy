from core.fields import UUIDExtractTimestamp
from core.models import SoftDeleteMixin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(SoftDeleteMixin, AbstractUser):
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.GeneratedField(
        verbose_name=_("date joined"),
        expression=UUIDExtractTimestamp("id"),
        output_field=models.DateTimeField(),
        db_persist=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["email", "is_active"], name="unique_email_is_active"
            )
        ]
