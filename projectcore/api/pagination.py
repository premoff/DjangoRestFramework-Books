from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

DEFAULT_PAGE = 5
DEFAULT_PAGE_SIZE = 10
class BookListPagination(PageNumberPagination):
    page_size = DEFAULT_PAGE
    page_size_query_param = 'page_size'
    max_page_size = DEFAULT_PAGE_SIZE

    def get_paginated_response(self, data):
        return Response({
            # 'links': {
            #     'next': self.get_next_link(),
            #     'previous': self.get_previous_link()
            # },
            'count': self.page.paginator.count,
            # 'page': int(self.request.GET.get('page', DEFAULT_PAGE)), # can not set default = self.page
            # 'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data
        })
