from core.fields import UUIDExtractTimestamp
from core.models import IdentityMixin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(IdentityMixin, AbstractUser):
    date_joined = models.GeneratedField(
        verbose_name=_("date joined"),
        expression=UUIDExtractTimestamp("id"),
        output_field=models.DateTimeField(),
        db_persist=True,
    )
