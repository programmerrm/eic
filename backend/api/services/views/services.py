from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from services.pagination import CumulativePagination
from services.models import Service, ServicePageTopBar, Schema, SeoTag
from api.services.serializers.services import (
    ServicePageTopBarSerializer,
    ServiceSerializer,
    SingleServiceSerializer,
    SeoTagSerializer,
    SchemaSerializer,
)

# ============= Contact SEO TAGS View =================
class SeoTagView(viewsets.ModelViewSet):
    queryset = SeoTag.objects.all()
    serializer_class = SeoTagSerializer

    CACHE_KEY = "contact_seotag_first"

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
                    'message': 'Contact seo tags data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = SeoTag.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Contact seo tags records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data
            cache.set(self.CACHE_KEY, data, timeout=60 * 60)
            return Response({
                'success': True,
                'message': 'Contact seo tags data fetching successfully.',
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

# ============= Contact SCHEMA View =================
class SchemaView(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer

    CACHE_KEY = "contact_schema_first"

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
                    'message': 'Contact schema data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = Schema.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Contact schema records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60 * 60)

            return Response({
                'success': True,
                'message': 'Contact schema data fetching successfully.',
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

class ServicePageTopBarView(viewsets.ModelViewSet):
    serializer_class = ServicePageTopBarSerializer
    queryset = ServicePageTopBar.objects.all()

    CACHE_KEY = "service_top_bar"

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
                    'message': 'Service top bar data fetched successfully.',
                    'data': cached_data,
                },status=status.HTTP_200_OK)
            obj = ServicePageTopBar.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Service top bar records not found',
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Service top bar data fetched successfully.',
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

class ServiceView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().order_by('-id')
    pagination_class = CumulativePagination

    CACHE_KEY_PREFIX = "service_items_list"
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
                    "message": "Service data fetched successfully.",
                    "data": serializer.data,
                }

                paginated_response = self.get_paginated_response(inner_results)

                cache.set(cache_key, paginated_response.data, timeout=self.CACHE_TIMEOUT)

                return paginated_response

            serializer = self.get_serializer(queryset, many=True)
            response_data = {
                "success": True,
                "message": "Service data fetched successfully.",
                "data": serializer.data,
            }
            cache.set(cache_key, response_data, timeout=self.CACHE_TIMEOUT)
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            })

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

class SingleServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = SingleServiceSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    CACHE_KEY_PREFIX = "single_service"
    CACHE_TIMEOUT = 60 * 60 

    def retrieve(self, request, *args, **kwargs):
        try:
            slug = kwargs.get(self.lookup_field)
            cache_key = f"{self.CACHE_KEY_PREFIX}_{slug}"

            cached_data = cache.get(cache_key)
            if cached_data:
                return Response(cached_data, status=status.HTTP_200_OK)

            service = self.get_object()
            serializer = self.get_serializer(service)

            response_data = {
                'success': True,
                'message': 'Single service fetched successfully.',
                'data': serializer.data,
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
        