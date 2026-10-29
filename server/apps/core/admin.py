import csv

from core.models import Directory
from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse


class ImportExportMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename={meta}.csv"
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response

    export_as_csv.short_description = "Export CSV selected"
    export_as_json.short_description = "View JSON selected"


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


actions = [
    (ImportExportMixin.export_as_csv, "export_as_csv"),
    (ImportExportMixin.export_as_json, "export_as_json"),
]

for target, name in actions:
    admin.site.add_action(target, name)
