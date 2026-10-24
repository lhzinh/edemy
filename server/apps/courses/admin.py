from courses.models import Course
from django.contrib import admin


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)
