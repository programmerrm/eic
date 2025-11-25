from rest_framework import viewsets
from services.models import Service, ServicePageTopBar
from api.services.serializers.services import ServicePageTopBarSerializer, ServiceSerializer, FaqSerializer, FaqItemSerializer

class ServicePageTopBarView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServicePageTopBarSerializer

    def get_queryset(self):
        obj = ServicePageTopBar.objects.first()
        if obj:
            return ServicePageTopBar.objects.filter(id=obj.id)
        return ServicePageTopBar.objects.none()

class ServiceView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class SingleServiceView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            return Service.objects.filter(slug=slug)
        return Service.objects.none()
    