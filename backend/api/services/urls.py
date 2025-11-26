# ==========================================
"""
CONFIGURATION ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from api.services.views.services import ServicePageTopBarView, ServiceView, SingleServiceView

router = DefaultRouter()

router.register(r'top-bar', ServicePageTopBarView, basename='service_page_top_bar')
router.register(r'list-items', ServiceView, basename='service')
router.register(r'single', SingleServiceView, basename='single_service')

urlpatterns = router.urls
