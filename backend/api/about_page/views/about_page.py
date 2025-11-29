from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from api.about_page.serializers.about_page import AboutTopBarSerializer
from about_page.models import AboutTopBar

# ============ ABOUT TOP BAR VIEW ===============
class AboutTopBarView(viewsets.ModelViewSet):
    serializer_class = AboutTopBarSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = AboutTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'About top bar records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'About top bar data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        