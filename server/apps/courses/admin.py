from typing import ClassVar

from core.admin import ImportExportMixin
from courses.models import Category, Course
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin, ImportExportMixin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin, ImportExportMixin):
    readonly_fields: ClassVar[list[str]] = [
        "creator",
        "changer",
        "date_created",
        "date_updated",
    ]

    def save_model(self, request, obj, form, change):
        obj.stamp(request.user)
        super().save_model(request, obj, form, change)
