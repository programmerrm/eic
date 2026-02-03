import logging
from django.db import DatabaseError
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView, ListAPIView

logger = logging.getLogger(__name__)

class BaseRetrieveView(RetrieveAPIView):
    related_fields = []
    permission_classes = [AllowAny]
    serializer_class = None
    CACHE_KEY = None
    CACHE_TIMEOUT = None
    empty_status_404 = True

    def get_object_instance(self):
        raise NotImplementedError("You must implement get_object_instance()")
    
    def get_object(self):
        try:
            qs = self.get_object_instance()
            if self.related_fields:
                qs = qs.select_related(*self.related_fields)
            obj = qs.first()
            return obj
        except DatabaseError as e:
            logger.error(f"Database error in {self.__class__.__name__}: {str(e)}")
            return None
    
    def retrieve(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)
        if cached_data is not None:
            return Response({
                "success": True,
                "message": f"{self.__class__.__name__} data retrieved from cache.",
                "data": cached_data,
            }, status=status.HTTP_200_OK)
        
        obj = self.get_object()
        if not obj:
            status_code = status.HTTP_404_NOT_FOUND if self.empty_status_404 else status.HTTP_200_OK
            logger.warning(f"{self.__class__.__name__} data not found")
            return Response({
                "success": False,
                "message": f"{self.__class__.__name__} data not found",
                "data": {},
            }, status=status_code)
        
        try:
            serializer = self.get_serializer(obj)
            cache.set(self.CACHE_KEY, serializer.data, self.CACHE_TIMEOUT)
            return Response({
                "success": True,
                "message": f"{self.__class__.__name__} data retrieved from database.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(f"Serialization error in {self.__class__.__name__}: {str(e)}")
            return Response({
                "success": False,
                "message": f"Error serializing data: {str(e)}",
                "data": {},
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BaseListView(ListAPIView):
    related_fields = []
    prefetch_fields = []
    permission_classes = [AllowAny]
    pagination_class = None
    serializer_class = None
    CACHE_KEY = None
    CACHE_TIMEOUT = None

    def get_queryset_instance(self):
        raise NotImplementedError("You must implement get_queryset_instance()")

    def get_queryset(self):
        try:
            qs = self.get_queryset_instance()
            if self.related_fields:
                qs = qs.select_related(*self.related_fields)
            if self.prefetch_fields:
                qs = qs.prefetch_related(*self.prefetch_fields)
            return qs
        except DatabaseError as e:
            logger.error(f"Database error in {self.__class__.__name__}: {str(e)}")
            return self.get_queryset_instance().none()
    
    def list(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)
        if cached_data is not None:
            return Response({
                "success": True,
                "message": f"{self.__class__.__name__} data fetched from cache.",
                "data": cached_data,
            }, status=status.HTTP_200_OK)

        queryset = self.get_queryset()
        if not queryset.exists():
            logger.warning(f"{self.__class__.__name__} data not found")
            return Response({
                "success": True,
                "message": f"No {self.__class__.__name__} data found",
                "data": [],
            }, status=status.HTTP_200_OK)
        
        try:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            cache.set(self.CACHE_KEY, data, self.CACHE_TIMEOUT)
            return Response({
                "success": True,
                "message": f"{self.__class__.__name__} data fetched from database.",
                "data": data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(f"Serialization error in {self.__class__.__name__}: {str(e)}")
            return Response({
                "success": False,
                "message": f"Error serializing data: {str(e)}",
                "data": [],
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
