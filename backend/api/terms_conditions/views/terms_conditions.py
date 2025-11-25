######################################################
"""
TERMS CONDITIONS ALL VIEWS
"""
######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from terms_conditions.models import TermsConditionTopBar, TermsConditionContent
from api.terms_conditions.serializers.terms_conditions import TermsConditionTopBarSerializer, TermsConditionContentSerializer

# ======== Terms Condition Top Bar VIEW ===========
class TermsConditionTopBarView(viewsets.ModelViewSet):
    serializer_class = TermsConditionTopBarSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = TermsConditionTopBar.objects.first()
            if queryset is None:
                return Response({
                    "message": "No terms condition top bar records found."
                }, status=status.HTTP_404_NOT_FOUND)
            return Response(TermsConditionTopBarSerializer(queryset).data, status=status.HTTP_200_OK)
        except TermsConditionTopBar.DoesNotExist:
            return Response({
                "message": "No terms condition top bar records found."
            }, status=status.HTTP_404_NOT_FOUND)
    
# ======== Terms Condition Content VIEW ===========
class TermsConditionContentView(viewsets.ModelViewSet):
    serializer_class = TermsConditionContentSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = TermsConditionContent.objects.first()
            if queryset is None:
                return Response({
                    "message": "No terms condition content records found."
                }, status=status.HTTP_404_NOT_FOUND)
            return Response(TermsConditionContentSerializer(queryset).data, status=status.HTTP_200_OK)
        except TermsConditionContent.DoesNotExist:
            return Response({
                "message": "No terms condition content records found."
            }, status=status.HTTP_404_NOT_FOUND)
    