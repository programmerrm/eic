# =====================================
"""
SUCCESS STORIES LIMIT PAGINATION
"""
# =====================================
from rest_framework.pagination import LimitOffsetPagination

class CumulativePagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 100

    def paginate_queryset(self, queryset, request, view=None):
        self.request = request
        self.count = queryset.count()

        self.limit = self.get_limit(request)
        self.offset = self.get_offset(request)

        end = self.offset + self.limit

        return list(queryset[:end])
    