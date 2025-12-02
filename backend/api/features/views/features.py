from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from django.core.cache import cache
from api.features.serializers.features import FeatureSerializer, FeatureItemSerializer
from features.models import Feature, FeatureItem

# ========== FEATURE VIEWSET =============
class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    CACHE_KEY = "feature_topbar"

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)
            if cached_data:
                return Response({
                    "success": True,
                    "message": "Feature data fetched successfully.",
                    "data": cached_data,
                }, status=status.HTTP_200_OK)
            obj = Feature.objects.first()
            if not obj:
                return Response({
                    "success": True,
                    "message": "No feature found.",
                    "data": []
                }, status=status.HTTP_200_OK)

            serializer = self.get_serializer(obj)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                "success": True,
                "message": "Feature data fetched successfully.",
                "data": data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
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

# ============ FEATURE ITEM VIEWSET =============
class FeatureItemViewSet(viewsets.ModelViewSet):
    queryset = FeatureItem.objects.all().order_by('-id')
    serializer_class = FeatureItemSerializer
    CACHE_KEY = "feature_topbar"

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            cached_data = cache.get(self.CACHE_KEY)
            if cached_data:
                return Response({
                    "success": True,
                    "message": "Feature items fetched successfully.",
                    "data": cached_data,
                }, status=status.HTTP_200_OK)
            obj = self.get_queryset()
            if not obj:
                return Response({
                    "success": True,
                    "message": "No feature items found.",
                    "data": []
                }, status=status.HTTP_200_OK)
            
            serializer = self.get_serializer(obj, many=True)
            data = serializer.data

            cache.set(self.CACHE_KEY, data, timeout=60*60)

            return Response({
                "success": True,
                "message": "Feature items fetched successfully.",
                "data": data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
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
        