from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.accounts.urls import router as accounts_router
from apps.courses.urls import router as courses_router

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
router.registry.extend(accounts_router.registry)
router.registry.extend(courses_router.registry)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # APIs
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

if settings.DEBUG and not settings.TESTING:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        re_path(r"^silk", include("silk.urls", namespace="silk")),
    ]
