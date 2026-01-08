from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from utils.is_admin_or_read_only import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from faq.models import FaqTopBar, FaqSection, FaqItem, Schema, SeoTag
from api.faq.serializers.faq import FaqItemSerializer, FaqSectionSerializer, FaqTopBarSerializer, SchemaSerializer, SeoTagSerializer
from faq.cache import FAQ_SEO_CACHE_KEY, FAQ_SCHEMA_CACHE_KEY, FAQ_TOP_BAR_CACHE_KEY, FAQ_SECTION_CACHE_KEY, FAQ_ITEMS_CACHE_KEY

# ========== FAQ TOP BAR VIEW SET ==============
class FaqTopBarView(viewsets.ModelViewSet):
    pepermission_classes = [IsAdminOrReadOnly]
    queryset = FaqTopBar.objects.all()
    serializer_class = FaqTopBarSerializer

    CACHE_KEY = FAQ_TOP_BAR_CACHE_KEY

    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)
            if cached_data:
                return Response({
                    'success': True,
                    'message': 'Faq top bar data fetched from cache.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            
            obj = FaqTopBar.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Faq top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60 * 60)

            return Response({
                'success': True,
                'message': 'Faq top bar data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ========== FAQ SECTION VIEW SET ==============
class FaqSectionView(viewsets.ModelViewSet):
    queryset = FaqSection.objects.all().order_by('-id')
    serializer_class = FaqSectionSerializer

    CACHE_KEY = FAQ_SECTION_CACHE_KEY

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
                    'message': 'Faq section top bar data fetched from cache.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)

            obj = FaqSection.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Faq section top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60 * 60)

            return Response({
                'success': True,
                'message': 'Faq section top bar data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ========== FAQ ITEM VIEW SET (ALL ITEMS) ==============
class FaqItemView(viewsets.ModelViewSet):
    queryset = FaqItem.objects.all().order_by('-id')
    serializer_class = FaqItemSerializer

    CACHE_KEY = FAQ_ITEMS_CACHE_KEY

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        """Faq all items"""
        try:
            cached_data = cache.get(self.CACHE_KEY)
            if cached_data:
                return Response({
                    "success": True,
                    "message": "Faq items fetched successfully from cache.",
                    "data": cached_data
                }, status=status.HTTP_200_OK)

            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60 * 60)

            return Response({
                "success": True,
                "message": "Faq items fetched successfully.",
                "data": data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ========== SCHEMA VIEW SET ==============
class SchemaViewSet(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer

    CACHE_KEY = FAQ_SCHEMA_CACHE_KEY

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
                    'message': 'Faq schema data fetched from cache.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)

            obj = Schema.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Faq schema records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60 * 60)

            return Response({
                'success': True,
                'message': 'Faq schema data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ======== SEO VIEW SET ==================
class SeoTagViewSet(viewsets.ModelViewSet):
    queryset = SeoTag.objects.all()
    serializer_class = SeoTagSerializer

    CACHE_KEY = FAQ_SEO_CACHE_KEY

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
                    'message': 'Faq seo tags data fetched from cache.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)

            obj = SeoTag.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Faq seo tags records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60 * 60)

            return Response({
                'success': True,
                'message': 'Faq seo tags data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
