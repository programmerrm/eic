# ==========================================
"""
PAGES ALL VIEW SET
"""
# ==========================================
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from api.pages.serializers.pages import PagesSerilizer
from pages.models import Pages

# ================== PAGES VIEW SET =================
class PagesViewSet(viewsets.ModelViewSet):
    queryset = Pages.objects.all()
    serializer_class = PagesSerilizer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = Pages.objects.all()
            if not queryset.exists():
                return Response({
                    "success": True,
                    "message": "No pages records found.",
                    "data": [],
                }, status=status.HTTP_200_OK)
            serialized_data = PagesSerilizer(queryset, many=True).data
            return Response({
                "success": True,
                "message": "",
                "data": serialized_data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    