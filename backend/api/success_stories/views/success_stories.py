######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from success_stories.pagination import CumulativePagination
from success_stories.models import SuccessStorieTopBar, SuccessStorie
from api.success_stories.serializers.success_stories import SuccessStorieTopBarSerializer, SuccessStorieSerializer, SingleSuccessStorieSerializer

class SuccessStorieTopBarView(viewsets.ModelViewSet):
    serializer_class = SuccessStorieTopBarSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = SuccessStorieTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Success storie top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Success storie top bar data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SuccessStorieView(viewsets.ModelViewSet):
    serializer_class = SuccessStorieSerializer
    pagination_class = CumulativePagination
    queryset = SuccessStorie.objects.all().order_by('-id')

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            page = self.paginate_queryset(self.queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response({
                    'success': True,
                    'message': 'Success storie data fetched successfully.',
                    'data': serializer.data,
                })
            serializer = self.get_serializer(self.queryset, many=True)
            return Response({
                'success': True,
                'message': 'Success storie data fetched successfully.',
                'data': serializer.data,
            })
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            })

class SingleSuccessStorieView(viewsets.ModelViewSet):
    queryset = SuccessStorie.objects.all()
    serializer_class = SingleSuccessStorieSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"