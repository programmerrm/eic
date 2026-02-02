from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
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

# ============ ABOUT TOP BAR VIEW ===============
class AboutTopBarView(viewsets.ModelViewSet):
    serializer_class = AboutTopBarSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    CACHE_KEY = ABOUT_TOP_BAR_CACHE_KEY
    
    def list(self, request, *args, **kwargs):
        try:
            
            cached_data = cache.get(self.CACHE_KEY)

            if cached_data:
                return Response({
                    'success': True,
                    'message': 'About top bar data fetching from cache successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)

            obj = AboutTopBar.objects.first()
            if not obj:
                return Response({
                    'success': True,
                    'message': 'About top bar records not found',
                    'data': {},
                }, status=status.HTTP_204_NO_CONTENT)
            
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=PAGE_CACHE_TIMEOUT)

            return Response({
                'success': True,
                'message': 'About top bar data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ============ Secure Future TopBar TOP BAR VIEW ===============
class SecureFutureTopBarView(viewsets.ModelViewSet):
    serializer_class = SecureFutureTopBarSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    CACHE_KEY = ABOUT_SECURE_FUTURE_TOP_BAR_CACHE_KEY
    
    def list(self, request, *args, **kwargs):
        try:

            cached_data = cache.get(self.CACHE_KEY)

            if cached_data:
                return Response({
                    'success': True,
                    'message': 'Secure Future top bar data fetching from cache successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)

            obj = SecureFutureTopBar.objects.first()
            if not obj:
                return Response({
                    'success': True,
                    'message': 'Secure Future Top Bar top bar records not found',
                    'data': {},
                }, status=status.HTTP_204_NO_CONTENT)
            
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=PAGE_CACHE_TIMEOUT)

            return Response({
                'success': True,
                'message': 'Secure Future top bar data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# =========== Secure Future Item =============
class SecureFutureItemView(viewsets.ModelViewSet):
    serializer_class = SecureFutureItemSerializer
    queryset = SecureFutureItem.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    CACHE_KEY = ABOUT_SECURE_FUTURE_ITEMS_CACHE_KEY
    
    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)

            if cached_data:
                return Response({
                    "success": True,
                    "message": "SecureFuture Item items fetched from cache successfully.",
                    "data": cached_data,
                }, status=status.HTTP_200_OK)

            obj = self.get_queryset()

            if not obj:
                return Response({
                    'success': True,
                    'message': 'Secure Future items records not found',
                    'data': [],
                }, status=status.HTTP_204_NO_CONTENT)

            serializer = self.serializer_class(obj, many=True)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=PAGE_CACHE_TIMEOUT)

            return Response({
                "success": True,
                "message": "SecureFuture Item items fetched successfully.",
                "data": data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

# =============== SecurityFirm =================
class SecurityFirmView(viewsets.ModelViewSet):
    serializer_class = SecurityFirmSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    CACHE_KEY = ABOUT_SECURITY_FIRM_CACHE_KEY
    
    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)

            if cached_data:
                return Response({
                    'success': True,
                    'message': 'Security Firm data fetching from cache successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            
            obj = SecurityFirm.objects.first()

            if not obj:
                return Response({
                    'success': True,
                    'message': 'Security Firm records not found',
                    'data': {},
                }, status=status.HTTP_204_NO_CONTENT)
            
            serializer = self.serializer_class(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=PAGE_CACHE_TIMEOUT)

            return Response({
                'success': True,
                'message': 'Security Firm data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# =========== DigitalSecuritySolutionTopBar ==========
class DigitalSecuritySolutionTopBarView(viewsets.ModelViewSet):
    serializer_class = DigitalSecuritySolutionTopBarSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    CACHE_KEY = ABOUT_DIGITAL_SECURITY_SOLUTION_TOP_BAR_CACHE_KEY
    
    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)

            if cached_data:
                return Response({
                    'success': True,
                    'message': 'DigitalSecurity Solution top bar data fetching from cache successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)

            queryset = DigitalSecuritySolutionTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': True,
                    'message': 'DigitalSecurity Solution top bar records not found',
                    'data': {},
                }, status=status.HTTP_204_NO_CONTENT)
            
            serializer = self.serializer_class(queryset)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=PAGE_CACHE_TIMEOUT)

            return Response({
                'success': True,
                'message': 'DigitalSecurity Solution top bar data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# ============ DigitalSecuritySolutionItem =============
class DigitalSecuritySolutionItemView(viewsets.ModelViewSet):
    serializer_class = DigitalSecuritySolutionItemSerializer
    queryset = DigitalSecuritySolutionItem.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    CACHE_KEY = ABOUT_DIGITAL_SECURITY_SOLUTION_ITEMS_CACHE_KEY
    
    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)

            if cached_data:
                return Response({
                    "success": True,
                    "message": "DigitalSecuritySolution items fetched from cache successfully.",
                    "data": cached_data,
                }, status=status.HTTP_200_OK)

            queryset = self.get_queryset()

            if not queryset:
                return Response({
                    "success": True,
                    "message": "DigitalSecuritySolution items no recoads.",
                    "data": [],
                }, status=status.HTTP_204_NO_CONTENT)

            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=PAGE_CACHE_TIMEOUT)

            return Response({
                "success": True,
                "message": "DigitalSecuritySolution items fetched successfully.",
                "data": data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

# ============ HappyJourneyTopBar ============
class HappyJourneyTopBarView(viewsets.ModelViewSet):
    serializer_class = HappyJourneyTopBarSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    CACHE_KEY = ABOUT_HAPPY_JOURNEY_TOP_BAR_CACHE_KEY
    
    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)
            if cached_data:
                return Response({
                    'success': True,
                    'message': 'Happy Journey top bar data fetching successfully.',
                    'data': cached_data,
                }, status=status.HTTP_200_OK)
            queryset = HappyJourneyTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': True,
                    'message': 'Happy Journey top bar records not found',
                    'data': {},
                }, status=status.HTTP_204_NO_CONTENT)
            serializer = self.serializer_class(queryset)
            data = serializer.data
            cache.set(self.CACHE_KEY, data, timeout=PAGE_CACHE_TIMEOUT)
            return Response({
                'success': True,
                'message': 'Happy Journey top bar data fetching successfully.',
                'data': data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ============== HappyJourneyItem ==============
class HappyJourneyItemView(viewsets.ModelViewSet):
    serializer_class = HappyJourneyItemSerializer
    queryset = HappyJourneyItem.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    CACHE_KEY = ABOUT_HAPPY_JOURNEY_ITEMS_CACHE_KEY
    
    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)
            if cached_data:
                return Response({
                    "success": True,
                    "message": "HappyJourney items fetched from cache successfully.",
                    "data": cached_data,
                }, status=status.HTTP_200_OK)
            queryset = self.get_queryset()
            if not queryset:
                return Response({
                    "success": True,
                    "message": "HappyJourney items fetched successfully.",
                    "data": [],
                }, status=status.HTTP_204_NO_CONTENT)
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=PAGE_CACHE_TIMEOUT)

            return Response({
                "success": True,
                "message": "HappyJourney items fetched successfully.",
                "data": data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
