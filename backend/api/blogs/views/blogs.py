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
    SeoTagSerializer, 
    SchemaSerializer, 
    RelatedBlogSerializer,
)
from blogs.models import (
    BlogTopBar, 
    Blog, 
    Schema, 
    SeoTag
)

# ============= Blog SEO TAGS View =================
class SeoTagView(viewsets.ModelViewSet):
    queryset = SeoTag.objects.all()
    serializer_class = SeoTagSerializer

    CACHE_KEY = "blog_seotag_first"

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)
            if cached_data:
                return Response({
                    'success': True,
                    'message': 'Blog seo tags data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = SeoTag.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Blog seo tags records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Blog seo tags data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        instance = serializer.save()
        cache.delete(self.CACHE_KEY)
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        cache.delete(self.CACHE_KEY)
        return instance

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.delete(self.CACHE_KEY)

# ============= Blog SCHEMA View =================
class SchemaView(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer

    CACHE_KEY = "blog_schema_first"

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)
            if cached_data:
                return Response({
                    'success': True,
                    'message': 'Blog schema data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = Schema.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Blog schema records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Blog schema data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        instance = serializer.save()
        cache.delete(self.CACHE_KEY)
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        cache.delete(self.CACHE_KEY)
        return instance

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.delete(self.CACHE_KEY)

# ============ BLOG TOP BAR VIEW ===============
class BlogTopBarView(viewsets.ModelViewSet):
    queryset = BlogTopBar.objects.all()
    serializer_class = BlogTopBarSerializer

    CACHE_KEY = "blog_topbar_first"

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)
            if cached_data:
                return Response({
                    'success': True,
                    'message': 'Blog top bar data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = BlogTopBar.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Blog top bar records not found',
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Blog top bar data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        instance = serializer.save()
        cache.delete(self.CACHE_KEY)
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        cache.delete(self.CACHE_KEY)
        return instance

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.delete(self.CACHE_KEY)

# ============ BLOG VIEW ===============
class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    pagination_class = CumulativePagination
    queryset = Blog.objects.all().order_by('-id')

    CACHE_KEY_PREFIX = "blog_items_list"
    CACHE_TIMEOUT = 60 * 60

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            query_string = request.META.get("QUERY_STRING", "")
            cache_key = f"{self.CACHE_KEY_PREFIX}_{query_string or 'no_params'}"

            cached_data = cache.get(cache_key)
            if cached_data:
                return Response(cached_data, status=status.HTTP_200_OK)

            queryset = self.get_queryset()
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)

                inner_results = {
                    "success": True,
                    "message": "Blog data fetched successfully.",
                    "data": serializer.data,
                }

                paginated_response = self.get_paginated_response(inner_results)

                cache.set(cache_key, paginated_response.data, timeout=self.CACHE_TIMEOUT)

                return paginated_response

            serializer = self.get_serializer(queryset, many=True)
            response_data = {
                "success": True,
                "message": "Blog data fetched successfully.",
                "data": serializer.data,
            }
            cache.set(cache_key, response_data, timeout=self.CACHE_TIMEOUT)
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "success": False,
                "message": "Something went wrong.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # ===== cache clear helper =====
    def _clear_blog_cache(self):
        try:
            from django_redis import get_redis_connection
            redis = get_redis_connection("default")
            keys = redis.keys(f"{self.CACHE_KEY_PREFIX}_*")
            if keys:
                redis.delete(*keys)
        except Exception:
            cache.clear()

    def perform_create(self, serializer):
        instance = serializer.save()
        self._clear_blog_cache()
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        self._clear_blog_cache()
        return instance

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        self._clear_blog_cache()
        
# ============ SINGLE BLOG VIEW ===============
class SingleBlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = SingleBlogSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    CACHE_KEY_PREFIX = "single_blog"
    CACHE_TIMEOUT = 60 * 60 

    def retrieve(self, request, *args, **kwargs):
        try:
            slug = kwargs.get(self.lookup_field)
            cache_key = f"{self.CACHE_KEY_PREFIX}_{slug}"

            cached_data = cache.get(cache_key)
            if cached_data:
                return Response(cached_data, status=status.HTTP_200_OK)

            blog = self.get_object()
            serializer = self.get_serializer(blog)

            tag_ids = blog.tags.values_list('id', flat=True)

            related_blogs = (
                Blog.objects.filter(tags__in=tag_ids)
                .exclude(id=blog.id)
                .distinct()
                .order_by('-created_at')[:6]
            )
            related_serializer = RelatedBlogSerializer(related_blogs, many=True)

            response_data = {
                'success': True,
                'message': 'Single blog fetched successfully.',
                'data': serializer.data,
                'related_blogs': related_serializer.data
            }

            cache.set(cache_key, response_data, timeout=self.CACHE_TIMEOUT)

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _clear_single_cache(self, slug):
        cache_key = f"{self.CACHE_KEY_PREFIX}_{slug}"
        cache.delete(cache_key)

    def perform_update(self, serializer):
        instance = serializer.save()
        self._clear_single_cache(instance.slug)
        return instance

    def perform_destroy(self, instance):
        slug = instance.slug
        super().perform_destroy(instance)
        self._clear_single_cache(slug)
