from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from api.about_page.serializers.about_page import (
    AboutTopBarSerializer,
    SecureFutureItemSerializer,
    SecureFutureTopBarSerializer,
    SecurityFirmSerializer,
    DigitalSecuritySolutionTopBarSerializer,
    DigitalSecuritySolutionItemSerializer,
    HappyJourneyTopBarSerializer,
    HappyJourneyItemSerializer,
)
from about_page.models import (
    AboutTopBar, 
    SecureFutureTopBar, 
    SecureFutureItem,
    SecurityFirm,
    DigitalSecuritySolutionTopBar,
    DigitalSecuritySolutionItem,
    HappyJourneyTopBar,
    HappyJourneyItem,
)
from about_page.cache import (
    ABOUT_DIGITAL_SECURITY_SOLUTION_ITEMS_CACHE_KEY,
    ABOUT_DIGITAL_SECURITY_SOLUTION_TOP_BAR_CACHE_KEY,
    ABOUT_HAPPY_JOURNEY_ITEMS_CACHE_KEY,
    ABOUT_HAPPY_JOURNEY_TOP_BAR_CACHE_KEY,
    ABOUT_SECURE_FUTURE_ITEMS_CACHE_KEY,
    ABOUT_SECURE_FUTURE_TOP_BAR_CACHE_KEY,
    ABOUT_SECURITY_FIRM_CACHE_KEY,
    ABOUT_TOP_BAR_CACHE_KEY,
    PAGE_CACHE_TIMEOUT,
)

# ============ About Top Bar  ===============
class AboutTopBarView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = AboutTopBarSerializer
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT
    CACHE_KEY = ABOUT_TOP_BAR_CACHE_KEY

    def get_object(self):
        return get_object_or_404(
            AboutTopBar.objects.only(
                'id', 'title', 'description'
            )
        )
    
    def retrieve(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)
        if cached_data is not None:
            return Response({
                'success': True,
                'message': 'About top bar data retrieved successfully from cache.',
                'data': cached_data,
            }, status=status.HTTP_200_OK)
        
        obj = self.get_object()
        serializer = self.get_serializer(obj)

        cache.set(self.CACHE_KEY, serializer.data, self.CACHE_TIMEOUT)

        return Response({
            "success": True,
            "message": "About top bar retrieved from database",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

# ============ Secure Future Top Bar ===============
class SecureFutureTopBarView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = SecureFutureTopBarSerializer
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT
    CACHE_KEY = ABOUT_SECURE_FUTURE_TOP_BAR_CACHE_KEY

    def get_object(self):
        return get_object_or_404(
            SecureFutureTopBar.objects.only(
                'id', 'normal_title', 'title_span'
            )
        )

    def retrieve(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)
        if cached_data is not None:
            return Response({
                'success': True,
                'message': 'Secure Future top bar data retrieved successfully from cache.',
                'data': cached_data,
            }, status=status.HTTP_200_OK)
        
        obj = self.get_object()
        serializer = self.get_serializer(obj)

        cache.set(self.CACHE_KEY, serializer.data, self.CACHE_TIMEOUT)

        return Response({
            "success": True,
            "message": "Secure Future top bar retrieved from database",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
# =========== Secure Future Items =============
class SecureFutureItemView(ListAPIView):
    pagination_class = None
    permission_classes = [AllowAny]
    serializer_class = SecureFutureItemSerializer
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT
    CACHE_KEY = ABOUT_SECURE_FUTURE_ITEMS_CACHE_KEY

    def get_queryset(self):
        return SecureFutureItem.objects.only(
            'id', 'title', 'image', 'alt', 'description'
        )
    
    def list(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)

        if cached_data is not None:
            return Response({
                "success": True,
                "message": "Secure future items fetched from cache successfully.",
                "data": cached_data,
        }, status=status.HTTP_200_OK)

        queryset = self.get_queryset()

        if not queryset.exists():
            return Response({
                "success": True,
                "message": "Secure future item not found",
                "data": [],
            }, status=status.HTTP_200_OK)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        cache.set(self.CACHE_KEY, data, self.CACHE_TIMEOUT)

        return Response({
            "success": True,
            "message": "Secure future items fetched successfully.",
            "data": data,
        }, status=status.HTTP_200_OK)

# =============== Security Firm =================
class SecurityFirmView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = SecurityFirmSerializer
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT
    CACHE_KEY = ABOUT_SECURITY_FIRM_CACHE_KEY

    def get_object(self):
        return get_object_or_404(
            SecurityFirm.objects.only(
                'id', 'bg', 'bg_image_alt', 'main_img', 'main_image_alt', 'title_span', 'title_normal', 'mission_title', 'mission_description', 'vision_title', 'vision_description', 'get_to_know_us_btn_name', 'get_to_know_us_btn_url'
            )
        )

    def retrieve(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)
        if cached_data is not None:
            return Response({
                'success': True,
                'message': 'Security firm data retrieved successfully from cache.',
                'data': cached_data,
            }, status=status.HTTP_200_OK)
        
        obj = self.get_object()
        serializer = self.get_serializer(obj)

        cache.set(self.CACHE_KEY, serializer.data, self.CACHE_TIMEOUT)

        return Response({
            "success": True,
            "message": "Security firm data retrieved from database",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

# =========== Digital Security Solution Top Bar ==========
class DigitalSecuritySolutionTopBarView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = DigitalSecuritySolutionTopBarSerializer
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT
    CACHE_KEY = ABOUT_DIGITAL_SECURITY_SOLUTION_TOP_BAR_CACHE_KEY

    def get_object(self):
        return get_object_or_404(
            DigitalSecuritySolutionTopBar.objects.only(
                'id', 'title', 'description'
            )
        )
    
    def retrieve(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)
        if cached_data is not None:
            return Response({
                'success': True,
                'message': 'Digital security solution top bar data retrieved successfully from cache.',
                'data': cached_data,
            }, status=status.HTTP_200_OK)
        
        obj = self.get_object()
        serializer = self.get_serializer(obj)

        cache.set(self.CACHE_KEY, serializer.data, self.CACHE_TIMEOUT)

        return Response({
            "success": True,
            "message": "Digital security solution top bar data retrieved from database",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
# ============ Digital Security Solution Items =============
class DigitalSecuritySolutionItemView(ListAPIView):
    pagination_class = None
    permission_classes = [AllowAny]
    serializer_class = DigitalSecuritySolutionItemSerializer
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT
    CACHE_KEY = ABOUT_DIGITAL_SECURITY_SOLUTION_ITEMS_CACHE_KEY

    def get_queryset(self):
        return DigitalSecuritySolutionItem.objects.only(
            'id', 'count', 'title', 'description'
        )
    
    def list(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)

        if cached_data is not None:
            return Response({
                "success": True,
                "message": "Digital security solution items fetched from cache successfully.",
                "data": cached_data,
        }, status=status.HTTP_200_OK)

        queryset = self.get_queryset()

        if not queryset.exists():
            return Response({
                "success": True,
                "message": "Digital security solution item not found",
                "data": [],
            }, status=status.HTTP_200_OK)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        cache.set(self.CACHE_KEY, data, self.CACHE_TIMEOUT)

        return Response({
            "success": True,
            "message": "Digital security solution items fetched successfully.",
            "data": data,
        }, status=status.HTTP_200_OK)

# ============ Happy Journey Top Bar ============
class HappyJourneyTopBarView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = HappyJourneyTopBarSerializer
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT
    CACHE_KEY = ABOUT_HAPPY_JOURNEY_TOP_BAR_CACHE_KEY

    def get_object(self):
        return get_object_or_404(
            HappyJourneyTopBar.objects.only(
                'id', 'title'
            )
        )
    
    def retrieve(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)
        if cached_data is not None:
            return Response({
                'success': True,
                'message': 'Happy journey top bar data retrieved successfully from cache.',
                'data': cached_data,
            }, status=status.HTTP_200_OK)
        
        obj = self.get_object()
        serializer = self.get_serializer(obj)

        cache.set(self.CACHE_KEY, serializer.data, self.CACHE_TIMEOUT)

        return Response({
            "success": True,
            "message": "Happy journey top bar data retrieved from database",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

# ============== Happy Journey Items ==============
class HappyJourneyItemView(ListAPIView):
    pagination_class = None
    permission_classes = [AllowAny]
    serializer_class = HappyJourneyItemSerializer
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT
    CACHE_KEY = ABOUT_HAPPY_JOURNEY_ITEMS_CACHE_KEY

    def get_queryset(self):
        return HappyJourneyItem.objects.only(
            'id', 'year', 'title', 'description'
        )
    
    def list(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)

        if cached_data is not None:
            return Response({
                "success": True,
                "message": "Happy journey items fetched from cache successfully.",
                "data": cached_data,
        }, status=status.HTTP_200_OK)

        queryset = self.get_queryset()

        if not queryset.exists():
            return Response({
                "success": True,
                "message": "Happy journey item not found",
                "data": [],
            }, status=status.HTTP_200_OK)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        cache.set(self.CACHE_KEY, data, self.CACHE_TIMEOUT)

        return Response({
            "success": True,
            "message": "Happy journey items fetched successfully.",
            "data": data,
        }, status=status.HTTP_200_OK)
