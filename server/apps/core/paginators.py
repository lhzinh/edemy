from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DynamicPagination(PageNumberPagination):
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "total": self.page.paginator.count,
                "size": self.page_size,
                "results": data,
            }
        )


class LargeResultsSetPagination(DynamicPagination):
    page_size = 1000
    max_page_size = 10000


class StandardResultsSetPagination(DynamicPagination):
    page_size = 2
    max_page_size = 1000
