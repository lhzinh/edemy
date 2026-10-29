from core.forms import FileImportForm
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _


class AdminSite(admin.AdminSite):
    site_header = "Edemy administration"

    def get_app_list(self, request, app_label=None):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_list = super().get_app_list(request, app_label)
        app_list += [
            {
                "name": _("Summary"),
                "app_label": "summary",
                "app_url": "/admin/summary/",
                "has_module_perms": True,
                "models": [
                    {
                        "name": _("Statistics"),
                        "object_name": "statistics",
                        "admin_url": reverse("admin:statistics"),
                        "view_only": True,
                    }
                ],
            }
        ]
        return sorted(app_list, key=lambda x: x["name"].lower())

    def statistics_view(self, request):
        context = dict(
            self.each_context(request),
            title=_("Statistics"),
        )
        return TemplateResponse(request, "admin/statistics.html", context)

    def get_urls(self):
        return [
            path(
                "summary/statistics/",
                self.admin_view(self.statistics_view, cacheable=True),
                name="statistics",
            ),
            path(
                "import/",
                self.admin_view(self.import_file, cacheable=True),
                name="import",
            ),
        ] + super().get_urls()

    def import_file(self, request):
        if request.method == "POST":
            file_source = request.FILES["file_source"]
            reader = csv.reader(file_source)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = FileImportForm()
        payload = {"form": form}
        return render(request, "admin/file_form.html", payload)
