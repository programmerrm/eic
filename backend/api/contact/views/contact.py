######################################################
"""
CONTACT ALL VIEWS
"""
######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from contact.models import (
    ContactTopBar, 
    ContactForm, 
    ConatctInfomation, 
    GoogleMap, 
    SeoTag, 
    Schema,
)
from api.contact.serializers.contact import (
    ContactTopBarSerializer, 
    ContactFormSerializer, 
    ConatctInfomationSerializer, 
    GoogleMapSerializer, 
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

# ============= Contact Top Bar View =================
class ContactTopBarView(viewsets.ModelViewSet):
    queryset = ContactTopBar.objects.all()
    serializer_class = ContactTopBarSerializer

    CACHE_KEY = "contact_topbar_first"

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
                    'message': 'Contact top bar data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)

            obj = ContactTopBar.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Contact top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Contact top bar data fetching successfully.',
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

# ============ Contact Form View ================
class ContactFormView(viewsets.ModelViewSet):
    serializer_class = ContactFormSerializer
    queryset = ContactForm.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                'success': True,
                'message': 'Your contact form has been submitted successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Failed to submit contact form.',
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

# =========== Conatct Infomation ===============
class ConatctInfomationView(viewsets.ModelViewSet):
    queryset = ConatctInfomation.objects.all()
    serializer_class = ConatctInfomationSerializer

    CACHE_KEY = "contact_infomation_first"

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
                    'message': 'Conatct infomation data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = ConatctInfomation.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Conatct infomation not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Conatct infomation data fetching successfully.',
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

# ============== Google Map View ============
class GoogleMapView(viewsets.ModelViewSet):
    queryset = GoogleMap.objects.all()
    serializer_class = GoogleMapSerializer

    CACHE_KEY = "contact_googlemap_first"

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
                    'message': 'Google map data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = GoogleMap.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Google map not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Google map data fetching successfully.',
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
