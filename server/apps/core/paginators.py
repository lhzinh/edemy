from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class GenericPagination(PageNumberPagination):
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "per_page": self.get_page_size(self.request),
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results": data,
            }
        )

    def get_paginated_response_schema(self, schema):
        schema = super().get_paginated_response_schema(schema)
        schema["required"].append("per_page")
        schema["properties"]["per_page"] = {
            "type": "integer",
            "example": 10,
        }
        return schema


class LargeResultsSetPagination(GenericPagination):
    page_size = 1000
    max_page_size = 10000


class StandardResultsSetPagination(GenericPagination):
    page_size = 2
    max_page_size = 1000
