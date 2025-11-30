from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from faq.models import FaqTopBar, FaqSection, FaqItem
from api.faq.serializers.faq import FaqItemSerializer, FaqSectionSerializer, FaqTopBarSerializer

class FaqTopBarView(viewsets.ModelViewSet):
    serializer_class = FaqTopBarSerializer
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = FaqTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Faq top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Faq top bar data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FaqSectionView(viewsets.ModelViewSet):
    serializer_class = FaqSectionSerializer
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = FaqSection.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Faq section top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Faq section top bar data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FaqItemView(viewsets.ModelViewSet):
    serializer_class = FaqItemSerializer
    queryset = FaqItem.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        """Faqall items"""
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "success": True,
                "message": "Faq items fetched successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        