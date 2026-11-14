from courses.views import CategoryViewSet, CourseViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"courses", CourseViewSet, basename="course")
