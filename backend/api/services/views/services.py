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
from services.cache import (
    SERVICE_SEO_TAGS_CACHE_KEY,
    SERVICE_SCHEMA_CACHE_KEY,
    SERVICE_PAGE_TOP_BAR_CACHE_KEY,
    ALL_SERVICES_CACHE_KEY,
)

# ============= Contact SEO TAGS View =================
class SeoTagView(viewsets.ModelViewSet):
    queryset = SeoTag.objects.all()
    serializer_class = SeoTagSerializer

    CACHE_KEY = SERVICE_SEO_TAGS_CACHE_KEY

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
                    'message': 'Service seo tags data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = SeoTag.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Service seo tags records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data
            cache.set(self.CACHE_KEY, data, timeout=60 * 60)
            return Response({
                'success': True,
                'message': 'Service seo tags data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ============= Contact SCHEMA View =================
class SchemaView(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer

    CACHE_KEY = SERVICE_SCHEMA_CACHE_KEY

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
                    'message': 'Service schema data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = Schema.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Service schema records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60 * 60)

            return Response({
                'success': True,
                'message': 'Service schema data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ServicePageTopBarView(viewsets.ModelViewSet):
    serializer_class = ServicePageTopBarSerializer
    queryset = ServicePageTopBar.objects.all()

    CACHE_KEY = SERVICE_PAGE_TOP_BAR_CACHE_KEY

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

class ServiceView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().order_by('-id')
    pagination_class = CumulativePagination

    CACHE_KEY_PREFIX = ALL_SERVICES_CACHE_KEY
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

class SingleServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = SingleServiceSerializer
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        try:
            service = self.get_object()
            serializer = self.get_serializer(service)
            response_data = {
                'success': True,
                'message': 'Single service fetched successfully.',
                'data': serializer.data,
            }
            return Response(
                response_data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
