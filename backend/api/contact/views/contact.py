######################################################
"""
CONTACT ALL VIEWS
"""
######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
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
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({
                'success': False,
                'message': 'Validation failed.',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        contact = serializer.save()

        context = {
            'full_name': contact.full_name,
            'email': contact.email,
            'phone_number': contact.phone_number,
            'company_name': contact.company_name,
            'message': contact.message,
        }

        html_content = render_to_string('emails/contact_email.html', context)
        text_content = strip_tags(html_content)

        subject = f"New contact form submission from {contact.full_name}"
        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', settings.EMAIL_HOST_USER)
        to_emails = [getattr(settings, 'SITE_ADMIN_EMAIL', settings.EMAIL_HOST_USER)]

        try:
            msg = EmailMultiAlternatives(
                subject,
                text_content,
                from_email,
                to_emails,
                reply_to=[contact.email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send(fail_silently=False)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Failed to send email.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            'success': True,
            'message': 'Your contact form has been submitted successfully.',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

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
