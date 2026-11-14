from courses.models import Category, Course
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify


class Command(BaseCommand):
    help = "Seeds the database with sample categories and courses"

    def __init__(self, *args, **kwargs):
        self.data = {
            "Web Development": ["React", "Vue", "Next.js"],
            "Languages / Platforms": ["Python", "C++"],
            "AI & Machine Learning": ["Vibe Coding", "Data Engineer"],
        }
        super().__init__(*args, **kwargs)

    @transaction.atomic
    def handle(self, *args, **options):
        Category.objects.bulk_create(
            [Category(slug=slugify(name), name=name) for name in self.data],
            ignore_conflicts=True,
        )
        temp = {c.name: c for c in Category.objects.filter(name__in=self.data)}

        Course.objects.bulk_create(
            [
                Course(slug=slugify(course), name=course, category=temp[category])
                for category, courses in self.data.items()
                for course in courses
            ],
            ignore_conflicts=True,
        )

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database."))
