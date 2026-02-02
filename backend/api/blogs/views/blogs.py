######################################################
"""
BLOGS ALL VIEWS
"""
######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from blogs.pagination import CumulativePagination
from api.blogs.serializers.blogs import (
    BlogTopBarSerializer, 
    BlogSerializer, 
    SingleBlogSerializer,
    RelatedBlogSerializer,
)
from blogs.models import (
    BlogTopBar, 
    Blog,
)
from blogs.cache import BLOG_TOP_BAR_CACHE_KEY, ALL_BLOGS_CACHE_KEY, SINGLE_BLOG_CACHE_KEY

# ============ BLOG TOP BAR VIEW ===============
class BlogTopBarView(viewsets.ModelViewSet):
    queryset = BlogTopBar.objects.all()
    serializer_class = BlogTopBarSerializer

    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        cached_data = cache.get(BLOG_TOP_BAR_CACHE_KEY)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        obj = BlogTopBar.objects.first()
        if not obj:
            return Response({
                "success": False,
                "message": "Blog top bar not found"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(obj)

        response_data = {
            "success": True,
            "message": "Blog top bar fetched successfully",
            "data": serializer.data
        }

        cache.set(BLOG_TOP_BAR_CACHE_KEY, response_data, timeout=60 * 60)

        return Response(response_data, status=status.HTTP_200_OK)

# ============ BLOG VIEW ===============
class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    pagination_class = CumulativePagination
    queryset = Blog.objects.all().order_by("-id")

    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        query_string = request.META.get("QUERY_STRING", "no_params")
        cache_key = f"{ALL_BLOGS_CACHE_KEY}_{query_string}"

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            inner_data = {
                "success": True,
                "message": "Blogs fetched successfully",
                "data": serializer.data
            }

            response = self.get_paginated_response(inner_data)
            cache.set(cache_key, response.data, timeout=60 * 60)

            return response

        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            "success": True,
            "message": "Blogs fetched successfully",
            "data": serializer.data
        }

        cache.set(cache_key, response_data, timeout=60 * 60)

        return Response(response_data, status=status.HTTP_200_OK)
   
# ============ SINGLE BLOG VIEW ===============
class SingleBlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = SingleBlogSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        cache_key = f"{SINGLE_BLOG_CACHE_KEY}_{slug}"

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        blog = self.get_object()
        serializer = self.get_serializer(blog)

        tag_ids = blog.tags.values_list("id", flat=True)

        related_blogs = (
            Blog.objects.filter(tags__in=tag_ids)
            .exclude(id=blog.id)
            .distinct()
            .order_by("-created_at")[:6]
        )

        related_serializer = RelatedBlogSerializer(related_blogs, many=True)

        response_data = {
            "success": True,
            "message": "Single blog fetched successfully",
            "data": serializer.data,
            "related_blogs": related_serializer.data
        }

        cache.set(cache_key, response_data, timeout=60 * 60)

        return Response(response_data, status=status.HTTP_200_OK)
