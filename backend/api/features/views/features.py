from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from django.core.cache import cache
from features.models import Feature, FeatureItem
from api.features.serializers.features import FeatureSerializer, FeatureItemSerializer
from features.cache import FEATURE_CACHE_KEY, FEATURE_ITEM_CACHE_KEY

# -------------------------------
# Feature ViewSet
# -------------------------------
class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    CACHE_KEY = FEATURE_CACHE_KEY

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)
        if cached_data is not None:
            return Response({
                "success": True,
                "message": "Feature data fetched from cache",
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

        cache.set(self.CACHE_KEY, data, timeout=60*60)  # 1 hour
        return Response({
            "success": True,
            "message": "Feature data fetched from DB",
            "data": data
        }, status=status.HTTP_200_OK)

# -------------------------------
# FeatureItem ViewSet
# -------------------------------
class FeatureItemViewSet(viewsets.ModelViewSet):
    queryset = FeatureItem.objects.all().order_by('-id')
    serializer_class = FeatureItemSerializer
    CACHE_KEY = FEATURE_ITEM_CACHE_KEY

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)
        if cached_data is not None:
            return Response({
                "success": True,
                "message": "Feature items fetched from cache",
                "data": cached_data,
            }, status=status.HTTP_200_OK)

        obj = self.get_queryset()
        if not obj.exists():
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
            "message": "Feature items fetched from DB",
            "data": data
        }, status=status.HTTP_200_OK)
