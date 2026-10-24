from django.core.management.base import BaseCommand

from courses.models import Course


class Command(BaseCommand):
    help = "Seeds the database with sample categories and courses"

    def handle(self, *args, **options):
        # Create courses
        # authors = [
        #     Author(
        #         name="J.R.R. Tolkien",
        #         bio="The creator of Middle-earth and author of The Lord of the Rings.",
        #     ),
        #     Author(
        #         name="George R.R. Martin",
        #         bio="The author of the epic fantasy series A Song of Ice and Fire.",
        #     ),
        #     Author(name="J.K. Rowling", bio="The creator of the Harry Potter series."),
        # ]
        # Author.objects.bulk_create(authors)

        # # Create books
        # books = [
        #     Book(title="The Fellowship of the Ring", author=authors[0]),
        #     Book(title="The Two Towers", author=authors[0]),
        #     Book(title="The Return of the King", author=authors[0]),
        #     Book(title="A Game of Thrones", author=authors[1]),
        #     Book(title="A Clash of Kings", author=authors[1]),
        #     Book(title="Harry Potter and the Philosopher's Stone", author=authors[2]),
        #     Book(title="Harry Potter and the Chamber of Secrets", author=authors[2]),
        # ]
        # Book.objects.bulk_create(books)

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database."))
