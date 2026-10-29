from decimal import Decimal
from typing import ClassVar

from core.models import ActiveMixin, AuditMixin, GeneratorSEOMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(AuditMixin, ActiveMixin, GeneratorSEOMixin):
    name = models.CharField(_("name"), max_length=80, unique=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self) -> str:
        return self.name


class Course(AuditMixin, ActiveMixin, GeneratorSEOMixin):
    categories = models.ManyToManyField(
        Category,
        verbose_name=_("list of categories"),
        related_name="%(class)s",
        blank=True
    )
    title = models.CharField(_("title"), max_length=120)
    description = models.TextField(_("description"))
    price = models.DecimalField(
        max_digits=10, decimal_places=3, default=Decimal("0.000")
    )
    image = models.ImageField(upload_to="courses/%Y/%m/%d", null=True, blank=True)

    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")
        indexes: ClassVar[list[models.Index]] = [
            models.Index(fields=["title"]),
            models.Index(fields=["is_active", "-date_created"]),
            models.Index(fields=["price"]),
        ]

    def __str__(self) -> str:
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=1)


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=1)
