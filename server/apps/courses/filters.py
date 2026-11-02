import django_filters
from courses.models import Course


class CourseFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name="categories__slug", label="Category"
    )
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Course
        fields = ["category", "max_price", "min_price"]
