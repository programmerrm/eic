# ==========================================
"""
PAGES ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from api.pages.views.pages import PagesViewSet

router = DefaultRouter()
router.register(r'menus', PagesViewSet, basename='pages')

urlpatterns = router.urls
