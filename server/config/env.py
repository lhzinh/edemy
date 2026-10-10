import os

from config.settings import base


def get_settings_module():
    """Set settings module"""

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        f"config.settings.{'local' if base.DEBUG else 'production'}",
    )
