from core.fields import UUIDExtractTimestamp, UUIDField
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class IdentityMixin(models.Model):
    """Abstract base class providing `id` fields"""

    id = UUIDField(primary_key=True, version=7)

    class Meta:
        abstract = True


class TimeStampedMixin(IdentityMixin):
    """Abstract base class providing `date_created` and `date_modified` fields"""

    date_created = models.GeneratedField(
        verbose_name=_("date created"),
        expression=UUIDExtractTimestamp("id"),
        output_field=models.DateTimeField(),
        db_persist=True,
    )
    date_modified = models.DateTimeField(verbose_name=_("date modified"), auto_now=True)

    class Meta:
        abstract = True


class AuditMixin(models.Model):
    """Abstract base class providing `creator` and `modifier` fields"""

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="%(class)s_creator",
    )
    modifier = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="%(class)s_modifier",
    )

    class Meta:
        abstract = True
