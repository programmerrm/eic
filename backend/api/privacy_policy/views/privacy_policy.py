######################################################
"""
PRIVACY POLICY ALL VIEWS
"""
######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from privacy_policy.models import PrivacyPolicyTopBar, PrivacyPolicyContent
from api.privacy_policy.serializers.privacy_policy import PrivacyPolicyTopBarSerializer, PrivacyPolicyContentSerializer

# ======== Privacy Policy Top Bar VIEW ===========
class PrivacyPolicyTopBarView(viewsets.ModelViewSet):
    serializer_class = PrivacyPolicyTopBarSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = PrivacyPolicyTopBar.objects.first()
            if queryset is None:
                return Response({
                    "message": "No privacy policy top bar records found."
                }, status=status.HTTP_404_NOT_FOUND)
            return Response(PrivacyPolicyTopBarSerializer(queryset).data, status=status.HTTP_200_OK)
        except PrivacyPolicyTopBar.DoesNotExist:
            return Response({
                "message": "No privacy policy top bar records found."
            }, status=status.HTTP_404_NOT_FOUND)
    
# ======== Privacy Policy Content VIEW ===========
class PrivacyPolicyContentView(viewsets.ModelViewSet):
    serializer_class = PrivacyPolicyContentSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = PrivacyPolicyContent.objects.first()
            if queryset is None:
                return Response({
                    "message": "No privacy policy content records found."
                }, status=status.HTTP_404_NOT_FOUND)
            return Response(PrivacyPolicyContentSerializer(queryset).data, status=status.HTTP_200_OK)
        except PrivacyPolicyContent.DoesNotExist:
            return Response({
                "message": "No privacy policy content records found."
            }, status=status.HTTP_404_NOT_FOUND)
    