######################################################
"""
HOMEPAGE ALL VIEWS
"""
######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from api.homepage.serializers.homepage import (
    BannerSerializer,
    SecurityFirmSerializer, 
    CybersecuritySolutionTitleSerializer,
    CybersecuritySolutionItemSerializer,
    OurProvenProcessSecuritySerializer,
    OurProvenProcessSecurityItemsSerializer,
    PaymnetInfoSerializer,
    ReviewTopBarSerializer,
    ReviewSerializer,
    ExperienceEicSerializer,
    ExperienceEicItemSerializer,
    GloballyAccreditedSerializer,
    SchemaSerializer,
    SeoTagSerializer,
)
from homepage.models import (
    Banner,
    SecurityFirm,
    CybersecuritySolutionTitle,
    CybersecuritySolutionItem,
    OurProvenProcessSecurity,
    OurProvenProcessSecurityItems,
    PaymnetInfo,
    ReviewTopBar,
    Review,
    ExperienceEic,
    ExperienceEicItem,
    GloballyAccredited,
    SeoTag,
    Schema,
)

# ============= SEO TAGS View =================
class SeoTagView(viewsets.ModelViewSet):
    queryset = SeoTag.objects.all()
    serializer_class = SeoTagSerializer

    CACHE_KEY = "home_seotag_first"

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
                    'message': 'Homepage seo tags data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = SeoTag.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Homepage seo tags records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Homepage seo tags data fetching successfully.',
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

# ============= SCHEMA View =================
class SchemaView(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer

    CACHE_KEY = "home_schema_first"

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
                    'message': 'Homepage schema data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            obj = Schema.objects.first()
            if not obj:
                return Response({
                    'success': False,
                    'message': 'Homepage schema records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                'success': True,
                'message': 'Homepage schema data fetching successfully.',
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


# =========== BANNER VIEW SET =============
class BannerViewSet(viewsets.ModelViewSet):
    serializer_class = BannerSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = Banner.objects.first()
            if queryset is None:
                return Response({
                    "success": True,
                    "message": "No banner records found.",
                    "data": [],
                }, status=status.HTTP_200_OK)
            return Response({
                "success": True,
                "message": "banner data fetching", 
                "data": BannerSerializer(queryset).data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# =========== Paymnet Info VIEW SET =============
class PaymnetInfoViewSet(viewsets.ModelViewSet):
    serializer_class = PaymnetInfoSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = PaymnetInfo.objects.first()
            if queryset is None:
                return Response({
                    "success": True,
                    "message": "No paymnet info records found.",
                    "data": [],
                }, status=status.HTTP_200_OK)
            return Response({
                "success": True,
                "message": "paymnet info data fetching", 
                "data": PaymnetInfoSerializer(queryset).data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# =========== SECURITY FIRM VIEW SET =============
class SecurityFirmViewSet(viewsets.ModelViewSet):
    serializer_class = SecurityFirmSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = SecurityFirm.objects.first()
            if queryset is None:
                return Response({
                    "success": True,
                    "message": "No security firm records found.",
                    "data": [],
                }, status=status.HTTP_200_OK)
            return Response({
                "success": True,
                "message": "Security firm data fetching", 
                "data": SecurityFirmSerializer(queryset).data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CybersecuritySolutionTitleViewSet(viewsets.ModelViewSet):
    serializer_class = CybersecuritySolutionTitleSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = CybersecuritySolutionTitle.objects.first()
            if queryset is None:
                return Response({
                    "success": True,
                    "message": "No security firm records found.",
                    "data": [],
                }, status=status.HTTP_200_OK)
            return Response({
                "success": True,
                "message": "Security firm data fetching", 
                "data": CybersecuritySolutionTitleSerializer(queryset).data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CybersecuritySolutionItemViewSet(viewsets.ModelViewSet):
    queryset = CybersecuritySolutionItem.objects.all()
    serializer_class = CybersecuritySolutionItemSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        if not self.queryset.exists():
            return Response({"message": "No cyber security solution item records found."}, status=status.HTTP_404_NOT_FOUND)
        return super().list(request, *args, **kwargs)

class OurProvenProcessSecurityViewSet(viewsets.ModelViewSet):
    queryset = OurProvenProcessSecurity.objects.all()
    serializer_class = OurProvenProcessSecuritySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        first_record = OurProvenProcessSecurity.objects.first()

        if first_record is None:
            return Response({"message": "No our proven process security records found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(first_record)
        return Response({
            "success": True,
            "message": "Our Proven Process Security fetched successfully.",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)

class OurProvenProcessSecurityItemsViewSet(viewsets.ModelViewSet):
    queryset = OurProvenProcessSecurityItems.objects.all()
    serializer_class = OurProvenProcessSecurityItemsSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        if not self.queryset.exists():
            return Response({"message": "No our proven process security item records found."}, status=status.HTTP_404_NOT_FOUND)
        return super().list(request, *args, **kwargs)

class ReviewTopBarViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewTopBarSerializer
    queryset = ReviewTopBar.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = ReviewTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Review top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(queryset)
            return Response({
                'success': True,
                'message': 'Review top bar data fetched successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        """Review all items"""
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "success": True,
                "message": "Review items fetched successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ExperienceEicViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceEicSerializer
    queryset = ExperienceEic.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = ExperienceEic.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Experience Eic records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(queryset)
            return Response({
                'success': True,
                'message': 'Experience eic data fetched successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

class ExperienceEicItemViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceEicItemSerializer
    queryset = ExperienceEicItem.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        """Experience eic all items"""
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "success": True,
                "message": "Experience eic items fetched successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GloballyAccreditedViewSet(viewsets.ModelViewSet):
    serializer_class = GloballyAccreditedSerializer
    queryset = GloballyAccredited.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = GloballyAccredited.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Globally accredited records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(queryset)
            return Response({
                'success': True,
                'message': 'Globally accredited data fetched successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
