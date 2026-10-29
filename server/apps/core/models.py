from os.path import basename
from typing import Any, ClassVar
from urllib.parse import urlsplit

import requests
from core.managers import GenericManager
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class ImageFromURLMixin(models.Model):
    class Meta:
        abstract = True

    async def save_image_from_url(self, url):
        if self.image:
            await self.image.adelete(save=False)

        with NamedTemporaryFile(mode="wb+", delete=True) as tf:
            r = requests.get(url, stream=True)
            for chunk in r.iter_content(chunk_size=4096):
                if chunk:
                    tf.write(chunk)

            tf.flush()
            tf.seek(0)
            await self.image.asave(basename(urlsplit(url).path), File(tf))


class AuditMixin(models.Model):
    date_created = models.DateTimeField(
        _("date created"),
        auto_now_add=True,
        null=True,
        blank=True,
    )
    date_updated = models.DateTimeField(
        _("date updated"),
        auto_now=True,
        null=True,
        blank=True,
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("creator"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    changer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("changer"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    class Meta:
        abstract = True

    def stamp(self, user: Any) -> None:
        if self.pk is None:
            self.creator = user
        self.changer = user


class ActiveMixin(models.Model):
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this record is active. "
            "Unselect this instead of deleting the record."
        ),
    )

    objects = models.Manager()
    scalars = GenericManager()

    class Meta:
        abstract = True
        indexes: ClassVar[list[models.Index]] = [models.Index(fields=["is_active"])]

    def soft_delete(self):
        """Mark the record as deleted instead of deleting it"""
        self.is_active = False
        self.save(update_fields=["is_active"])


class GeneratorSEOMixin(models.Model):
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        abstract = True
        indexes: ClassVar[list[models.Index]] = [models.Index(fields=["slug"])]

    def generate(self) -> str:
        for field_name in ["title", "name", "label"]:
            if hasattr(self, field_name):
                return str(getattr(self, field_name))

    def save(self, *args, **kwargs):
        base = slugify(self.generate())
        if not (self.slug and self.slug.startswith(base)):
            self.slug = base
            temp = self.slug
            while self.__class__.objects.filter(slug=temp).exclude(pk=self.pk).exists():
                temp = f"{base}-{get_random_string(6)}"
            self.slug = temp
        super().save(*args, **kwargs)


class Directory(models.Model):
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        managed = False
        db_table = "entities_entity"
        verbose_name = _("directory")
        verbose_name_plural = _("directories")

    def __str__(self) -> str:
        return self.name
