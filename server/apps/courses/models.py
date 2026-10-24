from accounts.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    creator = models.ForeignKey(
        User,
        verbose_name=_("creator"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    title = models.CharField(_("title"), max_length=120)
    description = models.TextField(_("description"))
    date_created = models.DateTimeField(_("date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("date created"), auto_now=True)

    def __str__(self) -> str:
        return self.title
