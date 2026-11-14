from django_filters import rest_framework as filters
from django_filters.widgets import RangeWidget


class GenericRangeWidget(RangeWidget):
    suffixes = ["min", "max"]


class FilterSet(filters.FilterSet):
    @classmethod
    def filter_for_field(cls, f, name, lookup_expr):
        filter = super().filter_for_field(f, name, lookup_expr)
        filter.extra["help_text"] = f.help_text
        return filter
