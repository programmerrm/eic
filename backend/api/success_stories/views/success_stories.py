######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from success_stories.pagination import CumulativePagination
from success_stories.models import (
    Schema,
    SeoTag,
    SuccessStorieTopBar, 
    SuccessStorie,
)
from api.success_stories.serializers.success_stories import (
    SuccessStorieTopBarSerializer, 
    SuccessStorieSerializer, 
    SingleSuccessStorieSerializer,
    SchemaSerializer,
    SeoTagSerializer,
)
from success_stories.cache import SUCCESS_STORIES_SEO_TAG_CACHE_KEY, SUCCESS_STORIES_SCHEMA_CACHE_KEY, SUCCESS_STORIES_TOP_BAR_CACHE_KEY, ALL_SUCCESS_STORIES_CACHE_KEY

# ============= SEO TAGS View =================
class SeoTagView(viewsets.ModelViewSet):
    queryset = SeoTag.objects.all()
    serializer_class = SeoTagSerializer

    CACHE_KEY = SUCCESS_STORIES_SEO_TAG_CACHE_KEY

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
                    'message': 'Success Stories seo tags data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = SeoTag.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Success Stories seo tags records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Success Stories seo tags data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ============= SCHEMA View =================
class SchemaView(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer

    CACHE_KEY = SUCCESS_STORIES_SCHEMA_CACHE_KEY

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
                    'message': 'Success Stories schema data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = Schema.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Success Stories schema records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Success Stories schema data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SuccessStorieTopBarView(viewsets.ModelViewSet):
    queryset = SuccessStorieTopBar.objects.all()
    serializer_class = SuccessStorieTopBarSerializer

    CACHE_KEY = SUCCESS_STORIES_TOP_BAR_CACHE_KEY

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
                    'message': 'Success storie top bar data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = SuccessStorieTopBar.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Success storie top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Success storie top bar data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class SuccessStorieView(viewsets.ModelViewSet):
    serializer_class = SuccessStorieSerializer
    pagination_class = CumulativePagination
    queryset = SuccessStorie.objects.all().order_by('-id')

    CACHE_KEY_PREFIX = ALL_SUCCESS_STORIES_CACHE_KEY
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
                    "message": "Success storie data fetched successfully.",
                    "data": serializer.data,
                }

                paginated_response = self.get_paginated_response(inner_results)

                cache.set(cache_key, paginated_response.data, timeout=self.CACHE_TIMEOUT)

                return paginated_response
            
            serializer = self.get_serializer(queryset, many=True)
            response_data = {
                "success": True,
                "message": "Success storie data fetched successfully.",
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

class SingleSuccessStorieView(viewsets.ModelViewSet):
    queryset = SuccessStorie.objects.all()
    serializer_class = SingleSuccessStorieSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        try:
            success_storie = self.get_object()
            serializer = self.get_serializer(success_storie)

            response_data = {
                'success': True,
                'message': 'Single success storie fetched successfully.',
                'data': serializer.data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

