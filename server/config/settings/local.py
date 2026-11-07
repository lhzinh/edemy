from .base import *

TESTING = "test" in sys.argv or "PYTEST_VERSION" in os.environ

INTERNAL_IPS = ["127.0.0.1"]

if not TESTING:
    INSTALLED_APPS += ["debug_toolbar", "silk"]

    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        "silk.middleware.SilkyMiddleware",
    ]

    SILKY_META = True
    # Silk takes anything <0 as no limit
    SILKY_MAX_REQUEST_BODY_SIZE = -1
    # If response body>1024kb, ignore
    SILKY_MAX_RESPONSE_BODY_SIZE = 1024
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    }
