from os.path import basename
from urllib.parse import urlsplit

import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models


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
