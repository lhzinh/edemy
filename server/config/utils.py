import os

from config.settings import base


def configure_settings_module():
    """Dynamically chooses settings profile based on the system."""
    settings_module = f"config.settings.{'local' if base.DEBUG else 'production'}"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
