from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seeds the database with sample categories and courses"

    def handle(self, *args, **options):
        call_command("migrate", interactive=False)
        call_command("loaddata", "data")
        self.stdout.write(self.style.SUCCESS("Successfully seeded the database."))
