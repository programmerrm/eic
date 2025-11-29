from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from services.pagination import CumulativePagination
from services.models import Service, ServicePageTopBar
from api.services.serializers.services import (
    ServicePageTopBarSerializer,
    ServiceSerializer,
    SingleServiceSerializer,
)

class ServicePageTopBarView(viewsets.ModelViewSet):
    serializer_class = ServicePageTopBarSerializer
    queryset = ServicePageTopBar.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = ServicePageTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Service top bar records not found',
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(queryset)
            return Response({
                'success': True,
                'message': 'Service top bar data fetched successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ServiceView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().order_by('-id')
    permission_classes = [IsAdminUser]   # default
    pagination_class = CumulativePagination

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            page = self.paginate_queryset(self.get_queryset())
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response({
                    'success': True,
                    'message': 'Services data fetched successfully.',
                    'data': serializer.data,
                })

            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response({
                'success': True,
                'message': 'Services data fetched successfully.',
                'data': serializer.data,
            })

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            })


class SingleServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = SingleServiceSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        try:
            service = self.get_object()
            serializer = self.get_serializer(service)

            return Response({
                'success': True,
                'message': 'Single service fetched successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
