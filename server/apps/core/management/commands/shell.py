from django.apps import apps
from django.core.management.commands import shell


class Command(shell.Command):
    def get_auto_imports(self):
        models = [
            f"{m.__module__}.{m.__name__}"
            for m in apps.get_models()
            if m._meta.app_label in ["accounts", "courses", "common", "posts"]
        ]
        return (
            super().get_auto_imports()
            + models
            + [
                "django.urls.reverse",
                "django.urls.resolve",
            ]
        )
