######################################################
"""
HOMEPAGE ALL VIEWS
"""
######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from api.homepage.serializers.homepage import (
    BannerSerializer,
    SecurityFirmSerializer, 
    CybersecuritySolutionTitleSerializer,
    CybersecuritySolutionItemSerializer,
    OurProvenProcessSecuritySerializer,
    OurProvenProcessSecurityItemsSerializer,
    PaymnetInfoSerializer,
)
from homepage.models import (
    Banner,
    SecurityFirm,
    CybersecuritySolutionTitle,
    CybersecuritySolutionItem,
    OurProvenProcessSecurity,
    OurProvenProcessSecurityItems,
    PaymnetInfo,
)

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
    queryset = OurProvenProcessSecurity.objects.first()
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
    