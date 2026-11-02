from rest_framework.pagination import PageNumberPagination


class DynamicPagination(PageNumberPagination):
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data = {"page_size": self.page.paginator.per_page, **response.data}
        return response

    def get_paginated_response_schema(self, schema):
        base = super().get_paginated_response_schema(schema)
        base["properties"]["page_size"] = {"type": "integer", "example": 12}
        base["required"].append("page_size")
        return base


class LargeResultsSetPagination(DynamicPagination):
    page_size = 1000
    max_page_size = 10000


class StandardResultsSetPagination(DynamicPagination):
    page_size = 2
    max_page_size = 1000
