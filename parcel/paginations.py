from rest_framework.pagination import PageNumberPagination

class ParcelsPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_number'
    page_size_query_param = 'page_size'
    max_page_size = 100