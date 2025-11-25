######################################################
"""
CONTACT ALL VIEWS
"""
######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from contact.models import ContactTopBar, ContactForm, ConatctInfomation, GoogleMap, SeoTag, Schema
from api.contact.serializers.contact import ContactTopBarSerializer, ContactFormSerializer, ConatctInfomationSerializer, GoogleMapSerializer, SeoTagSerializer, SchemaSerializer

# ============= Contact SEO TAGS View =================
class SeoTagView(viewsets.ModelViewSet):
    serializer_class = SeoTagSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = SeoTag.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Contact seo tags records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Contact seo tags data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ============= Contact SCHEMA View =================
class SchemaView(viewsets.ModelViewSet):
    serializer_class = SchemaSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = Schema.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Contact schema records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Contact schema data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ============= Contact Top Bar View =================
class ContactTopBarView(viewsets.ModelViewSet):
    serializer_class = ContactTopBarSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = ContactTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Contact top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Contact top bar data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
    serializer_class = ConatctInfomationSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = ConatctInfomation.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Conatct infomation not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Conatct infomation data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ============== Google Map View ============
class GoogleMapView(viewsets.ModelViewSet):
    serializer_class = GoogleMapSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = GoogleMap.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Google map not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Google map data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
