from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from api.features.serializers.features import FeatureSerializer, FeatureItemSerializer
from features.models import Feature, FeatureItem


# ==========================
# FEATURE VIEWSET
# ==========================
class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    def get_permissions(self):
        # Anyone can GET, only admin can POST/PUT/DELETE
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        """Return only the first Feature (like a section)"""
        try:
            queryset = Feature.objects.first()
            if not queryset:
                return Response({
                    "success": True,
                    "message": "No feature found.",
                    "data": []
                }, status=status.HTTP_200_OK)

            serializer = self.get_serializer(queryset)
            return Response({
                "success": True,
                "message": "Feature data fetched successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ==========================
# FEATURE ITEM VIEWSET
# ==========================
class FeatureItemViewSet(viewsets.ModelViewSet):
    queryset = FeatureItem.objects.all().order_by('-id')
    serializer_class = FeatureItemSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        """Return all feature items"""
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "success": True,
                "message": "Feature items fetched successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
