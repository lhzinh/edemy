from core.models import Directory
from django.contrib import admin


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
