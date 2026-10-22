import os
import sys
from pathlib import Path

DJANGO_PROJECT_ROOT = Path(__file__).resolve().parent.parent
DJANGO_SETTINGS_MODULE = "config.settings.local"


def init(verbose=None):
    try:
        import nest_asyncio

        nest_asyncio.apply()
        if verbose:
            print("Applied nest_asyncio patch for Jupyter compatibility")
    except ImportError:
        if verbose:
            print("nest_asyncio not available, skipping patch")

    os.chdir(DJANGO_PROJECT_ROOT)
    sys.path.insert(0, str(DJANGO_PROJECT_ROOT))
    if verbose:
        print(f"Changed working directory to: {DJANGO_PROJECT_ROOT}")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    import django

    django.setup()
