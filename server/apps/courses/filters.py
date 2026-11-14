from core.filters import FilterSet, GenericRangeWidget
from courses.models import Course
from django_filters import rest_framework as filters


class CourseFilter(FilterSet):
    price = filters.RangeFilter(widget=GenericRangeWidget())
    category = filters.CharFilter(
        field_name="category__slug", lookup_expr="iexact", label="Category"
    )

    class Meta:
        model = Course
        fields = ["category", "price"]
