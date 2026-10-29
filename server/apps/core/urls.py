import inngest.django
from accounts.functions import sync_user
from core.views import LineChartJSONView
from courses.views import CategoryViewSet, CourseViewSet
from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from config.client import inngest_client

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"courses", CourseViewSet, basename="course")

urlpatterns = [
    path("", include(router.urls)),
    path("chart", LineChartJSONView.as_view(), name="line_chart_json"),
    inngest.django.serve(
        inngest_client,
        [sync_user],
    ),
]
