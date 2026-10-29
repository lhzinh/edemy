from core.paginators import StandardResultsSetPagination
from core.views import SEOFieldMixin
from courses.models import Category, Course
from courses.serializers import CategorySerializer, CourseSerializer
from rest_framework import viewsets


class CategoryViewSet(SEOFieldMixin, viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing categories.
    """

    serializer_class = CategorySerializer
    queryset = Category.scalars.all()


class CourseViewSet(SEOFieldMixin, viewsets.ModelViewSet):
    """
    A viewset for viewing and editing courses.
    """

    queryset = Course.scalars.all().order_by("-date_created")
    serializer_class = CourseSerializer
    pagination_class = StandardResultsSetPagination
