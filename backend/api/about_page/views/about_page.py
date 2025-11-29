from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
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

# ============ ABOUT TOP BAR VIEW ===============
class AboutTopBarView(viewsets.ModelViewSet):
    serializer_class = AboutTopBarSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = AboutTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'About top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'About top bar data fetching successfully.',
                'data': serializer.data,
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
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = SecureFutureTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Secure Future Top Bar top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Secure Future top bar data fetching successfully.',
                'data': serializer.data,
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
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "success": True,
                "message": "SecureFuture Item items fetched successfully.",
                "data": serializer.data
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
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = SecurityFirm.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Security Firm records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Security Firm data fetching successfully.',
                'data': serializer.data,
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
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = DigitalSecuritySolutionTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'DigitalSecurity Solution top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'DigitalSecurity Solution top bar data fetching successfully.',
                'data': serializer.data,
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
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "success": True,
                "message": "DigitalSecuritySolution items fetched successfully.",
                "data": serializer.data
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
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = HappyJourneyTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Happy Journey top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Happy Journey top bar data fetching successfully.',
                'data': serializer.data,
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
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "success": True,
                "message": "HappyJourney items fetched successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

