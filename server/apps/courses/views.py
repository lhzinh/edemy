from core.paginators import StandardResultsSetPagination
from courses.filters import CourseFilter
from courses.selectors import active_categories, active_courses
from courses.serializers import CategorySerializer, CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    This viewset automatically provides `list` actions.
    """

    lookup_field = "slug"
    queryset = active_categories()
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    lookup_field = "slug"
    queryset = active_courses()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ["name"]
    ordering_fields = ["name", "price"]
